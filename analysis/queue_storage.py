"""Hybrid in-memory and disk-backed work queue for memory spill control."""

from __future__ import annotations

import logging
import os
import pickle
import sqlite3
import threading
import time
from collections import deque
from typing import Any, Optional

logger = logging.getLogger(__name__)


class WorkQueue:
    """Simple interface for queue backends."""

    def put(self, item: Any) -> None:
        raise NotImplementedError

    def put_many(self, items: list[Any]) -> None:
        for item in items:
            self.put(item)

    def get(self) -> Any:
        raise NotImplementedError

    def get_many(self, limit: int) -> list[Any]:
        items: list[Any] = []
        while len(items) < limit:
            try:
                item = self.get()
            except IndexError:
                break
            items.append(item)
        return items

    def size(self) -> int:
        raise NotImplementedError

    def close(self) -> None:
        return None


class InMemoryQueue(WorkQueue):
    """Thread-safe FIFO queue backed by collections.deque."""

    def __init__(self) -> None:
        self._deque: deque[Any] = deque()
        self._lock = threading.Lock()

    def put(self, item: Any) -> None:
        with self._lock:
            self._deque.append(item)

    def get(self) -> Any:
        with self._lock:
            if not self._deque:
                raise IndexError("queue is empty")
            return self._deque.popleft()

    def size(self) -> int:
        with self._lock:
            return len(self._deque)


class DiskQueue(WorkQueue):
    """SQLite-backed FIFO queue that persists across restarts."""

    def __init__(self, path: str, *, create_tables: bool = True) -> None:
        self.path = path
        self._lock = threading.RLock()
        self._conn = sqlite3.connect(path, check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute("PRAGMA synchronous=NORMAL")
        self._conn.execute("PRAGMA temp_store=MEMORY")
        self._conn.execute("PRAGMA locking_mode=NORMAL")
        if create_tables:
            self._conn.execute(
                "CREATE TABLE IF NOT EXISTS queue (id INTEGER PRIMARY KEY AUTOINCREMENT, payload BLOB NOT NULL)"
            )
            self._conn.commit()

    def put(self, item: Any) -> None:
        payload = pickle.dumps(item, protocol=pickle.HIGHEST_PROTOCOL)
        with self._lock:
            try:
                self._conn.execute("INSERT INTO queue(payload) VALUES (?)", (payload,))
                self._conn.commit()
            except sqlite3.Error as exc:
                logger.exception("[QUEUE] disk insert failed: %s", exc)
                raise

    def put_many(self, items: list[Any]) -> None:
        if not items:
            return
        payloads = [(pickle.dumps(item, protocol=pickle.HIGHEST_PROTOCOL),) for item in items]
        with self._lock:
            try:
                self._conn.execute("BEGIN")
                self._conn.executemany("INSERT INTO queue(payload) VALUES (?)", payloads)
                self._conn.commit()
            except sqlite3.Error as exc:
                self._conn.rollback()
                logger.exception("[QUEUE] disk batch insert failed: %s", exc)
                raise

    def get(self) -> Any:
        with self._lock:
            try:
                row = self._conn.execute(
                    "SELECT id, payload FROM queue ORDER BY id LIMIT 1"
                ).fetchone()
                if row is None:
                    raise IndexError("queue is empty")
                self._conn.execute("DELETE FROM queue WHERE id = ?", (row["id"],))
                self._conn.commit()
                return pickle.loads(row["payload"])
            except sqlite3.Error as exc:
                logger.exception("[QUEUE] disk read failed: %s", exc)
                raise

    def get_many(self, limit: int) -> list[Any]:
        if limit <= 0:
            return []
        with self._lock:
            try:
                rows = self._conn.execute(
                    "SELECT id, payload FROM queue ORDER BY id LIMIT ?",
                    (limit,),
                ).fetchall()
                if not rows:
                    return []
                ids = [row["id"] for row in rows]
                self._conn.execute("BEGIN")
                self._conn.execute(
                    f"DELETE FROM queue WHERE id IN ({','.join('?' for _ in ids)})",
                    ids,
                )
                self._conn.commit()
                return [pickle.loads(row["payload"]) for row in rows]
            except sqlite3.Error as exc:
                self._conn.rollback()
                logger.exception("[QUEUE] disk batch read failed: %s", exc)
                raise

    def size(self) -> int:
        with self._lock:
            try:
                row = self._conn.execute("SELECT COUNT(*) AS cnt FROM queue").fetchone()
                return int(row["cnt"])
            except sqlite3.Error as exc:
                logger.exception("[QUEUE] disk size failed: %s", exc)
                raise

    def close(self) -> None:
        with self._lock:
            if self._conn is not None:
                self._conn.close()
                self._conn = None


class MemoryMonitor:
    """Cached memory monitor that uses psutil when available."""

    def __init__(self, threshold: int = 80, cache_interval_seconds: float = 0.5) -> None:
        self.threshold = max(1, min(95, int(threshold)))
        self._cache_interval_seconds = max(0.0, float(cache_interval_seconds))
        self._last_check = 0.0
        self._last_percent = 0.0
        self._lock = threading.Lock()

    def get_usage_percent(self) -> float:
        try:
            import psutil
        except ImportError:  # pragma: no cover
            return 0.0

        try:
            return float(psutil.Process().memory_percent())
        except Exception:  # pragma: no cover
            try:
                return float(psutil.virtual_memory().percent)
            except Exception:  # pragma: no cover
                return 0.0

    def should_spill(self) -> bool:
        now = time.time()
        with self._lock:
            if self._cache_interval_seconds > 0 and now - self._last_check < self._cache_interval_seconds:
                return self._last_percent >= self.threshold
            percent = self.get_usage_percent()
            self._last_check = now
            self._last_percent = percent
            return percent >= self.threshold


class HybridQueue(WorkQueue):
    """Queue that spills new work to disk once memory pressure reaches a threshold."""

    def __init__(
        self,
        *,
        memory_monitor: Optional[MemoryMonitor] = None,
        storage_path: Optional[str] = None,
        storage_backend: str = "sqlite",
    ) -> None:
        self.ram_queue = InMemoryQueue()
        self.disk_queue = None
        self.memory_monitor = memory_monitor or MemoryMonitor()
        self.storage_backend = (storage_backend or "sqlite").lower()
        self.storage_path = storage_path or "./spool.db"
        self._spill_active = False
        self._lock = threading.Lock()

        if self.storage_backend == "sqlite":
            self.disk_queue = DiskQueue(self.storage_path)
        else:
            raise ValueError(f"Unsupported storage backend: {self.storage_backend}")

    def _update_spill_state(self) -> None:
        should_spill = self.memory_monitor.should_spill()
        with self._lock:
            if should_spill and not self._spill_active:
                self._spill_active = True
                logger.info("[MEMORY] Spill-to-disk mode activated.")
            elif not should_spill and self._spill_active:
                self._spill_active = False
                logger.info("[MEMORY] Spill-to-disk mode deactivated.")

    def put(self, item: Any) -> None:
        self._update_spill_state()
        with self._lock:
            if self._spill_active:
                self.disk_queue.put(item)
            else:
                self.ram_queue.put(item)

    def put_many(self, items: list[Any]) -> None:
        if not items:
            return
        self._update_spill_state()
        with self._lock:
            if self._spill_active:
                self.disk_queue.put_many(items)
            else:
                for item in items:
                    self.ram_queue.put(item)

    def get(self) -> Any:
        with self._lock:
            if self.ram_queue.size():
                return self.ram_queue.get()
            return self.disk_queue.get()

    def get_many(self, limit: int) -> list[Any]:
        if limit <= 0:
            return []
        with self._lock:
            if self.ram_queue.size():
                items = []
                while len(items) < limit and self.ram_queue.size():
                    items.append(self.ram_queue.get())
                if len(items) < limit:
                    items.extend(self.disk_queue.get_many(limit - len(items)))
                return items
            return self.disk_queue.get_many(limit)

    def size(self) -> int:
        with self._lock:
            return self.ram_queue.size() + self.disk_queue.size()

    def close(self) -> None:
        with self._lock:
            if self.disk_queue is not None:
                self.disk_queue.close()
                self.disk_queue = None

    def log_sizes(self) -> None:
        logger.info("[QUEUE] RAM=%s DISK=%s", self.ram_queue.size(), self.disk_queue.size())

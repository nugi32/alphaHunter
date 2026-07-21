"""Hybrid in-memory and disk-backed work queue for memory spill control."""

from __future__ import annotations

import logging
import os
import pickle
import sqlite3
import sys
import tempfile
import threading
import time
import resource
from collections import deque
from pathlib import Path
from typing import Any, Optional

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _resolve_storage_path(storage_path: Optional[str]) -> str:
    if not storage_path:
        return str(PROJECT_ROOT / "spool.db")

    path = Path(storage_path).expanduser()
    if path.is_absolute():
        return str(path)
    return str((PROJECT_ROOT / path).resolve())


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

    def __init__(self, path: str, *, create_tables: bool = True, timeout: float = 30.0) -> None:
        self.path = path
        self._lock = threading.RLock()
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        self._conn = sqlite3.connect(path, check_same_thread=False, timeout=timeout)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute("PRAGMA journal_mode=WAL")
        self._conn.execute("PRAGMA synchronous=NORMAL")
        self._conn.execute("PRAGMA temp_store=MEMORY")
        self._conn.execute("PRAGMA locking_mode=NORMAL")
        self._conn.execute("PRAGMA busy_timeout=5000")
        if create_tables:
            self._conn.execute(
                "CREATE TABLE IF NOT EXISTS queue (id INTEGER PRIMARY KEY AUTOINCREMENT, payload BLOB NOT NULL)"
            )
            self._conn.commit()

    def _execute_with_retry(self, operation, *, retries: int = 3) -> Any:
        last_error: Optional[Exception] = None
        for attempt in range(retries):
            try:
                return operation()
            except sqlite3.OperationalError as exc:
                message = str(exc).lower()
                if "locked" not in message and "busy" not in message:
                    raise
                last_error = exc
                if attempt < retries - 1:
                    time.sleep(0.1 * (attempt + 1))
                    continue
                raise
        if last_error is not None:
            raise last_error
        raise RuntimeError("unreachable")

    def put(self, item: Any) -> None:
        payload = pickle.dumps(item, protocol=pickle.HIGHEST_PROTOCOL)
        with self._lock:
            try:
                self._execute_with_retry(
                    lambda: self._conn.execute("INSERT INTO queue(payload) VALUES (?)", (payload,))
                )
                self._execute_with_retry(lambda: self._conn.commit())
            except sqlite3.Error as exc:
                logger.exception("[QUEUE] disk insert failed: %s", exc)
                raise

    def put_many(self, items: list[Any]) -> None:
        if not items:
            return
        payloads = [(pickle.dumps(item, protocol=pickle.HIGHEST_PROTOCOL),) for item in items]
        with self._lock:
            try:
                self._execute_with_retry(lambda: self._conn.execute("BEGIN"))
                self._execute_with_retry(lambda: self._conn.executemany("INSERT INTO queue(payload) VALUES (?)", payloads))
                self._execute_with_retry(lambda: self._conn.commit())
            except sqlite3.Error as exc:
                try:
                    self._conn.rollback()
                except sqlite3.Error:
                    pass
                logger.exception("[QUEUE] disk batch insert failed: %s", exc)
                raise

    def get(self) -> Any:
        with self._lock:
            try:
                row = self._execute_with_retry(
                    lambda: self._conn.execute(
                        "SELECT id, payload FROM queue ORDER BY id LIMIT 1"
                    ).fetchone()
                )
                if row is None:
                    raise IndexError("queue is empty")
                self._execute_with_retry(lambda: self._conn.execute("DELETE FROM queue WHERE id = ?", (row["id"],)))
                self._execute_with_retry(lambda: self._conn.commit())
                return pickle.loads(row["payload"])
            except sqlite3.Error as exc:
                logger.exception("[QUEUE] disk read failed: %s", exc)
                raise

    def get_many(self, limit: int) -> list[Any]:
        if limit <= 0:
            return []
        with self._lock:
            try:
                rows = self._execute_with_retry(
                    lambda: self._conn.execute(
                        "SELECT id, payload FROM queue ORDER BY id LIMIT ?",
                        (limit,),
                    ).fetchall()
                )
                if not rows:
                    return []
                ids = [row["id"] for row in rows]
                self._execute_with_retry(lambda: self._conn.execute("BEGIN"))
                self._execute_with_retry(
                    lambda: self._conn.execute(
                        f"DELETE FROM queue WHERE id IN ({','.join('?' for _ in ids)})",
                        ids,
                    )
                )
                self._execute_with_retry(lambda: self._conn.commit())
                return [pickle.loads(row["payload"]) for row in rows]
            except sqlite3.Error as exc:
                try:
                    self._conn.rollback()
                except sqlite3.Error:
                    pass
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
            psutil = None

        if psutil is not None:
            try:
                return float(psutil.Process().memory_percent())
            except Exception:  # pragma: no cover
                try:
                    return float(psutil.virtual_memory().percent)
                except Exception:  # pragma: no cover
                    pass

        try:
            with open("/proc/self/status", "r", encoding="utf-8") as handle:
                rss_kb = None
                for line in handle:
                    if line.startswith("VmRSS:"):
                        rss_kb = int(line.split()[1])
                        break
                if rss_kb is not None:
                    with open("/proc/meminfo", "r", encoding="utf-8") as meminfo:
                        for mem_line in meminfo:
                            if mem_line.startswith("MemTotal:"):
                                total_kb = int(mem_line.split()[1])
                                if total_kb > 0:
                                    return min(100.0, max(0.0, (rss_kb / total_kb) * 100.0))
        except Exception:  # pragma: no cover
            pass

        try:
            usage = resource.getrusage(resource.RUSAGE_SELF)
            rss_kb = getattr(usage, "ru_maxrss", None)
            if rss_kb is None:
                raise RuntimeError("ru_maxrss unavailable")

            rss_bytes = rss_kb * 1024
            total_bytes = None
            try:
                total_bytes = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES")
            except (AttributeError, ValueError, OSError):
                total_bytes = None

            if total_bytes and total_bytes > 0:
                return min(100.0, max(0.0, (rss_bytes / total_bytes) * 100.0))
        except Exception:  # pragma: no cover
            pass

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

    _MAX_RAM_ITEMS = 5_000

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
        if storage_path:
            self.storage_path = _resolve_storage_path(storage_path)
        else:
            temp_dir = tempfile.gettempdir()
            self.storage_path = os.path.join(temp_dir, "alphaHunter-spool.db")
        self._spill_active = False
        self._lock = threading.Lock()

        if self.storage_backend == "sqlite":
            try:
                self.disk_queue = DiskQueue(self.storage_path)
                # Prefer the disk backend immediately once it is configured so the
                # SQLite file grows instead of staying empty while the process uses
                # RAM and swap.
                self._spill_active = True
            except sqlite3.Error as exc:
                logger.warning("[QUEUE] Falling back to in-memory queue because disk backend failed: %s", exc)
                self.disk_queue = None
                self._spill_active = False
        else:
            raise ValueError(f"Unsupported storage backend: {self.storage_backend}")

    def _update_spill_state(self) -> None:
        if self.disk_queue is None:
            with self._lock:
                self._spill_active = False
            return

        should_spill = self.memory_monitor.should_spill()
        with self._lock:
            if self._spill_active:
                return
            if should_spill or self.ram_queue.size() >= self._MAX_RAM_ITEMS:
                self._spill_active = True
                logger.info("[MEMORY] Spill-to-disk mode activated.")

    def put(self, item: Any) -> None:
        self._update_spill_state()
        with self._lock:
            if self._spill_active and self.disk_queue is not None:
                self.disk_queue.put(item)
            else:
                self.ram_queue.put(item)

    def put_many(self, items: list[Any]) -> None:
        if not items:
            return
        self._update_spill_state()
        with self._lock:
            if self._spill_active and self.disk_queue is not None:
                for batch in [items[i : i + 1000] for i in range(0, len(items), 1000)]:
                    self.disk_queue.put_many(batch)
            else:
                for item in items:
                    if self.ram_queue.size() >= self._MAX_RAM_ITEMS:
                        self._update_spill_state()
                        if self._spill_active and self.disk_queue is not None:
                            self.disk_queue.put(item)
                            continue
                    self.ram_queue.put(item)

    def get(self) -> Any:
        with self._lock:
            if self.ram_queue.size():
                return self.ram_queue.get()
            if self.disk_queue is None:
                raise IndexError("queue is empty")
            return self.disk_queue.get()

    def get_many(self, limit: int) -> list[Any]:
        if limit <= 0:
            return []
        with self._lock:
            if self.ram_queue.size():
                items = []
                while len(items) < limit and self.ram_queue.size():
                    items.append(self.ram_queue.get())
                if len(items) < limit and self.disk_queue is not None:
                    items.extend(self.disk_queue.get_many(min(1000, limit - len(items))))
                return items
            if self.disk_queue is None:
                return []
            return self.disk_queue.get_many(min(limit, 1000))

    def size(self) -> int:
        with self._lock:
            disk_size = self.disk_queue.size() if self.disk_queue is not None else 0
            return self.ram_queue.size() + disk_size

    def close(self) -> None:
        with self._lock:
            if self.disk_queue is not None:
                self.disk_queue.close()
                self.disk_queue = None

    def log_sizes(self) -> None:
        logger.info("[QUEUE] RAM=%s DISK=%s", self.ram_queue.size(), self.disk_queue.size())

import os
import sqlite3
import sys
import tempfile
import threading
import time
from types import SimpleNamespace

import pandas as pd
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from analysis.queue_storage import (
    DiskQueue,
    HybridQueue,
    InMemoryQueue,
    MemoryMonitor,
)


class StaticMemoryMonitor(MemoryMonitor):
    def __init__(self, percent: float, threshold: int = 80):
        super().__init__(threshold=threshold, cache_interval_seconds=0.0)
        self._percent = percent

    def get_usage_percent(self) -> float:
        return self._percent


def test_spill_activation_uses_disk_queue_when_threshold_reached(tmp_path):
    queue = HybridQueue(
        memory_monitor=StaticMemoryMonitor(95, threshold=80),
        storage_path=str(tmp_path / "spill.db"),
        storage_backend="sqlite",
    )

    queue.put({"item": 1})
    assert queue.ram_queue.size() == 0
    assert queue.disk_queue.size() == 1
    assert queue.get() == {"item": 1}
    queue.close()


def test_sqlite_backed_queue_uses_disk_immediately_when_configured(tmp_path):
    queue = HybridQueue(
        memory_monitor=StaticMemoryMonitor(0, threshold=80),
        storage_path=str(tmp_path / "immediate.db"),
        storage_backend="sqlite",
    )

    queue.put({"item": 1})
    assert queue.ram_queue.size() == 0
    assert queue.disk_queue.size() == 1
    assert queue.get() == {"item": 1}
    queue.close()


def test_queue_persistence_and_recovery_after_restart(tmp_path):
    path = tmp_path / "persist.db"
    queue = DiskQueue(str(path))
    queue.put({"item": "payload"})
    queue.close()

    reopened = DiskQueue(str(path))
    assert reopened.get() == {"item": "payload"}
    reopened.close()


def test_batch_operations_and_bulk_retrieval(tmp_path):
    queue = DiskQueue(str(tmp_path / "batch.db"))
    queue.put_many([{"n": 1}, {"n": 2}, {"n": 3}])
    assert queue.size() == 3
    assert queue.get_many(2) == [{"n": 1}, {"n": 2}]
    assert queue.size() == 1
    queue.close()


def test_concurrent_access_is_safe(tmp_path):
    queue = DiskQueue(str(tmp_path / "concurrent.db"))
    errors = []

    def producer():
        try:
            for i in range(50):
                queue.put(i)
        except Exception as exc:  # pragma: no cover
            errors.append(exc)

    threads = [threading.Thread(target=producer) for _ in range(4)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    assert not errors
    assert queue.size() == 200
    queue.close()


def test_disk_queue_retries_when_database_is_locked(tmp_path):
    path = tmp_path / "locked.db"
    queue = DiskQueue(str(path), timeout=0.5)

    queue.put({"item": "payload"})
    assert queue.get() == {"item": "payload"}
    queue.close()


def test_in_memory_queue_is_thread_safe():
    queue = InMemoryQueue()
    queue.put("a")
    queue.put("b")
    assert queue.get() == "a"
    assert queue.get() == "b"
    assert queue.size() == 0


def test_memory_monitor_falls_back_to_resource_usage(monkeypatch):
    monkeypatch.setitem(sys.modules, "psutil", None)

    import resource

    monkeypatch.setattr(resource, "getrusage", lambda *_args, **_kwargs: SimpleNamespace(ru_maxrss=2048))

    monitor = MemoryMonitor(threshold=80, cache_interval_seconds=0.0)
    assert monitor.get_usage_percent() > 0


def test_scan_all_combos_keeps_running_when_memory_is_high(monkeypatch):
    from analysis import condition_engine

    df = pd.DataFrame({"Close": [1, 2, 3], "EMA_21": [1, 2, 3]})
    payload = {
        "conditions": [
            {"name": "cond", "type": "cross", "col": "Close", "op": ">", "col2": "EMA_21"}
        ],
        "min_samples": 1,
        "memory_spill_threshold_percent": 10,
    }

    monkeypatch.setattr(condition_engine, "_get_memory_usage_percent", lambda: 100.0)
    monkeypatch.setattr(condition_engine, "apply_combo", lambda df, combo, evaluators: pd.Series([True, True, True]))

    results = condition_engine.scan_all_combos(df, [("cond",)], payload)

    assert len(results) == 1


def test_build_search_space_does_not_cap_low_memory_runs(tmp_path):
    from analysis.search_space import build_search_space

    payload = {
        "conditions": [{"name": f"cond_{i}"} for i in range(20)],
        "max_depth": 5,
        "max_combinations": 10_000_000,
        "memory_spill_threshold_percent": 30,
        "storage_backend": "sqlite",
        "storage_path": str(tmp_path / "search.db"),
    }

    queue = HybridQueue(
        memory_monitor=None,
        storage_path=str(tmp_path / "queue.db"),
        storage_backend="sqlite",
    )
    space = build_search_space(payload, queue=queue)

    assert space.stats["total"] > 20_000
    assert space.stats["by_depth"].get(5, 0) > 0
    queue.close()

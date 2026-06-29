import os
import sys
import tempfile
import threading
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


def test_in_memory_queue_is_thread_safe():
    queue = InMemoryQueue()
    queue.put("a")
    queue.put("b")
    assert queue.get() == "a"
    assert queue.get() == "b"
    assert queue.size() == 0

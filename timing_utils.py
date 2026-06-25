import sys
import time
import threading
from contextlib import contextmanager
from time import perf_counter


def log_step(message):
    print(f"[>] {message}", flush=True)


@contextmanager
def spinner(message="Processing"):
    stop_event = threading.Event()

    def animate():
        frames = "|/-\\"
        i = 0

        while not stop_event.is_set():
            sys.stdout.write(f"\r{message} {frames[i % len(frames)]}")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1

        sys.stdout.write(f"\r{message} ✓\n")
        sys.stdout.flush()

    thread = threading.Thread(target=animate, daemon=True)
    thread.start()

    try:
        yield
    finally:
        stop_event.set()
        thread.join()


@contextmanager
def timed_spinner(message="Processing"):
    start = perf_counter()

    with spinner(message):
        yield

    elapsed = perf_counter() - start
    print(f"[✓] {message} ({elapsed:.2f}s)", flush=True)
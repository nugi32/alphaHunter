import time

from loader import load_tf
from indicators import volume, atr, rsi, adx


df = load_tf('M1')
modules = [volume, atr, rsi, adx]

for module in modules:
    print(f"Starting {module.__name__}", flush=True)
    start = time.perf_counter()
    module.apply(df.copy())
    elapsed = time.perf_counter() - start
    print(f"Done {module.__name__}: {elapsed:.2f}s", flush=True)

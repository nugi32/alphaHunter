import argparse
import gc

import numpy as np
import pandas as pd

from loader import load_tf

from indicators import (
    adx,
    advanced,
    atr,
    bollinger,
    cci,
    fibonacci,
    ichimoku,
    macd,
    momentum,
    pivot_points,
    rsi,
    stochastic,
    trend_ma,
    volatility,
    volume,
)

from patterns import (
    candle_patterns,
    cluster_model,
    compression,
    market_structure,
    similarity_search,
    volatility_regime,
    window_builder,
)

from timeframe import correlation

indicator_modules = [
    trend_ma,
    macd,
    bollinger,
    rsi,
    stochastic,
    atr,
    adx,
    cci,
    momentum,
    volume,
    volatility,
    ichimoku,
    fibonacci,
    pivot_points,
    advanced,
]

pattern_modules = [
    candle_patterns,
    compression,
    volatility_regime,
    market_structure,
]

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
def timed_spinner(message):
    start = perf_counter()

    with spinner(message):
        yield

    elapsed = perf_counter() - start
    print(f"[✓] {message} ({elapsed:.2f}s)", flush=True)

def prepare(df):
    log_step("Applying indicators...")

    for module in indicator_modules:
        log_step(f"Indicator: {module.__name__}")
        df = module.apply(df)

    log_step("Applying patterns...")

    for module in pattern_modules:
        log_step(f"Pattern: {module.__name__}")
        df = module.apply(df)

    return df


def _cleanup():
    gc.collect()


def _parse_scalar(value):
    raw = str(value).strip()

    if raw.lower() in {"true", "false"}:
        return raw.lower() == "true"

    try:
        if "." in raw:
            return float(raw)

        return int(raw)
    except ValueError:
        return raw


def _parse_condition(condition):
    condition = condition.strip()

    for operator in (">=", "<=", "==", "!=", ">", "<", "="):
        if operator in condition:
            column, raw = condition.split(operator, 1)
            value = _parse_scalar(raw.strip())

            column = column.strip()

            def make_predicate(col, op, val, is_column):
                if is_column:
                    if op in ("==", "="):
                        return lambda df, c: df[c] == df[val]
                    if op == "!=":
                        return lambda df, c: df[c] != df[val]
                    if op == ">=":
                        return lambda df, c: df[c] >= df[val]
                    if op == "<=":
                        return lambda df, c: df[c] <= df[val]
                    if op == ">":
                        return lambda df, c: df[c] > df[val]
                    if op == "<":
                        return lambda df, c: df[c] < df[val]

                else:
                    if op in ("==", "="):
                        return lambda df, c, v=val: df[c] == v
                    if op == "!=":
                        return lambda df, c, v=val: df[c] != v
                    if op == ">=":
                        return lambda df, c, v=val: df[c] >= v
                    if op == "<=":
                        return lambda df, c, v=val: df[c] <= v
                    if op == ">":
                        return lambda df, c, v=val: df[c] > v
                    if op == "<":
                        return lambda df, c, v=val: df[c] < v

                raise ValueError(f"Unsupported operator: {op}")

            is_column_ref = isinstance(value, str)
            predicate = make_predicate(column, operator, value, is_column_ref)

            return column, predicate

    raise ValueError(f"Unsupported condition: {condition}")


def _build_pattern_mask(df, pattern_spec):
    if not pattern_spec:
        return pd.Series(False, index=df.index)

    mask = pd.Series(True, index=df.index)

    for condition in pattern_spec.split(","):
        column, predicate = _parse_condition(condition)
        # Handle both scalar and column-to-column comparisons
        result = predicate(df, column) # Object of type "None" cannot be called
        mask &= result

    return mask.fillna(False)


def _pattern_summary(df, pattern_spec):
    mask = _build_pattern_mask(df, pattern_spec)
    hits = df.loc[mask].copy()
    price_move = hits["Close"] - hits["Open"]

    if hits.empty:
        return {
            "pattern": pattern_spec,
            "count": 0,
            "price_move_mean": None,
            "price_move_median": None,
            "price_move_min": None,
            "price_move_max": None,
            "bull_count": 0,
            "bear_count": 0,
            "flat_count": 0,
            "sample_rows": hits.head(10),
        }

    # Get all available indicator columns
    indicator_cols = [col for col in hits.columns if col not in ["UTC", "Open", "High", "Low", "Close", "Volume", "Date", "Time"]]
    
    result = {
        "pattern": pattern_spec,
        "count": int(mask.sum()),
        "price_move_mean": float(price_move.mean()),
        "price_move_median": float(price_move.median()),
        "price_move_min": float(price_move.min()),
        "price_move_max": float(price_move.max()),
        "price_move_std": float(price_move.std()),
        "bull_count": int((price_move > 0).sum()),
        "bear_count": int((price_move < 0).sum()),
        "flat_count": int((price_move == 0).sum()),
        "bullish_percentage": float((price_move > 0).sum() / len(price_move) * 100) if len(price_move) > 0 else 0,
        "bearish_percentage": float((price_move < 0).sum() / len(price_move) * 100) if len(price_move) > 0 else 0,
    }
    
    # Add detailed sample rows with indicator values
    sample_rows = hits[["UTC", "Open", "Close", "High", "Low", "Volume"] + indicator_cols].head(10).copy()
    sample_rows["PriceMove"] = sample_rows["Close"] - sample_rows["Open"]
    result["sample_rows"] = sample_rows
    
    return result


def run_analysis(
    save_csv=False,
    csv_name="XAU_USD_single_timeframe.csv",
    timeframe="M1",
    pattern_spec=None,
):
    log_step(f"Starting analysis for timeframe: {timeframe}")

    # Load data
    with timed_spinner("Loading timeframe data"):
        df = load_tf(timeframe, limit=None)

    # Prepare indicators + patterns
    with timed_spinner("Preparing indicators and patterns"):
        df = prepare(df)

    _cleanup()

    # Merge / copy
    with timed_spinner("Building merged dataframe"):
        merged = df.copy()
        merged["TF_BULL_STACK"] = float("nan")
        merged["TF_BEAR_STACK"] = float("nan")

    # Window builder
    with timed_spinner("Building windows"):
        X = window_builder.build(merged)

    with timed_spinner("Dropping NaN rows"):
        X = X.dropna()

    with timed_spinner("Resolving valid rows"):
        valid_rows = merged.index[20:][X.index]

    # Cluster model
    with timed_spinner("Running clustering model"):
        model, labels = cluster_model.fit(X)

    # Similarity search
    with timed_spinner("Running similarity search"):
        similar = similarity_search.search(X)

    # Correlation
    with timed_spinner("Analyzing correlations"):
        correlations = correlation.analyze(merged)

    # Similar rows extraction
    with timed_spinner("Building similar rows output"):
        similar_rows = merged.loc[
            valid_rows[similar],
            [
                "UTC",
                "Close",
                "COMPRESSION",
                "VOL_REGIME",
                "TF_BULL_STACK",
                "TF_BEAR_STACK",
            ],
        ].copy()

    # Pattern summary
    if pattern_spec:
        with timed_spinner("Running pattern summary"):
            pattern_summary = _pattern_summary(merged, pattern_spec)
    else:
        pattern_summary = None

    # Cleanup
    with timed_spinner("Cleaning memory"):
        del X
        _cleanup()

    # Save CSV
    if save_csv:
        with timed_spinner(f"Saving CSV -> {csv_name}"):
            merged.to_csv(csv_name, index=False)

    log_step("Analysis complete")

    return {
        "data": {timeframe: merged},
        "merged": merged,
        "model": model,
        "labels": labels,
        "similar_indices": similar,
        "similar_rows": similar_rows,
        "tf_similarity_indices": None,
        "correlations": correlations,
        "pattern_summary": pattern_summary,
    }
    
def main():
    parser = argparse.ArgumentParser(description="Run alphaHunter analysis for a single timeframe")
    parser.add_argument(
        "--tf",
        default="M1",
        choices=["M1", "M5", "M15", "H1", "H4", "D1", "W1", "MN1"],
        help="Timeframe to analyze",
    )
    parser.add_argument(
        "--pattern",
        default=None,
        help="Pattern conditions to analyze, e.g. DOJI=1,COMPRESSION=1,VOL_REGIME=1 or RSI_14>70",
    )

    args = parser.parse_args()

    result = run_analysis(save_csv=True, timeframe=args.tf, pattern_spec=args.pattern)

    if result["pattern_summary"]:
        summary = result["pattern_summary"]
        print("\n" + "="*70)
        print("PATTERN ANALYSIS RESULTS")
        print("="*70)
        print(f"\nTimeframe: {args.tf}")
        print(f"Pattern Condition: {summary['pattern']}")
        print(f"\n--- OCCURRENCE STATISTICS ---")
        print(f"Total Occurrences: {summary['count']}")
        if summary['count'] > 0:
            print(f"Bullish (Close > Open): {summary['bull_count']} ({summary['bullish_percentage']:.2f}%)")
            print(f"Bearish (Close < Open): {summary['bear_count']} ({summary['bearish_percentage']:.2f}%)")
            print(f"Flat (Close = Open): {summary['flat_count']}")
            print(f"\n--- PRICE MOVEMENT ANALYSIS ---")
            print(f"Average Price Move: {summary['price_move_mean']:.6f}")
            print(f"Median Price Move: {summary['price_move_median']:.6f}")
            print(f"Std Dev Price Move: {summary['price_move_std']:.6f}")
            print(f"Min Price Move: {summary['price_move_min']:.6f}")
            print(f"Max Price Move: {summary['price_move_max']:.6f}")
            print(f"\n--- DETAILED SAMPLE OCCURRENCES (showing up to 10 examples) ---")
            print(summary["sample_rows"].to_string())
        else:
            print("No patterns found matching the condition.")
        print("\n" + "="*70)

    print("\n=== SIMILAR ROWS ===")
    print(result["similar_rows"])
    return result


if __name__ == "__main__":
    main()

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
    squeeze,
    stochastic,
    swing_levels,
    trend_ma,
    volatility,
    volume,
)

from patterns import (
    candle_patterns,
    cluster_model,
    compression,
    market_structure,
    pattern_discovery,
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
    squeeze,
    swing_levels,
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


def _get_column_aliases():
    """Return a mapping of common alias names to actual column patterns."""
    return {
        # MACD aliases
        "MACD": "MACD_12_26",
        "MACD_SIGNAL": "MACD_SIGNAL_9",
        "MACD_HIST": "MACD_HIST_12_26_9",
        
        # Stochastic aliases
        "STOCH_K": "STO_K_14",
        "STOCH_D": "STO_D_14",
        "STO_K": "STO_K_14",
        "STO_D": "STO_D_14",
        "K": "STO_K_14",
        "D": "STO_D_14",
        
        # Momentum aliases
        "MOMENTUM": "MOM_10",
        "MOM": "MOM_10",
        "ROC": "ROC_10",
        
        # Fibonacci aliases
        "FIB_236": "FIB_0.236",
        "FIB_382": "FIB_0.382",
        "FIB_5": "FIB_0.5",
        "FIB_618": "FIB_0.618",
        "FIB_786": "FIB_0.786",
        
        # RSI aliases
        "RSI": "RSI_14",
        
        # ADX aliases
        "ADX": "ADX_14",
        "DI_PLUS": "DI_PLUS_14",
        "DI_MINUS": "DI_MINUS_14",
        
        # ATR aliases
        "ATR": "ATR_14",
        
        # CCI aliases
        "CCI": "CCI_14",
        
        # Volume aliases
        "VOLUME_SPIKE": "VOL_SMA20",
        "VOL_SPIKE": "VOL_SMA20",
        
        # Squeeze aliases
        "SQUEEZE_ON": "SQUEEZE",
        
        # Market Structure aliases (Break of Structure)
        "BOS_BULL": "HH",
        "BOS_BEAR": "LL",
        "HH_BULL": "HH",
        "LL_BEAR": "LL",
    }


def _resolve_column_name(column, df):
    """Resolve column name using aliases or exact match."""
    # First try exact match
    if column in df.columns:
        return column
    
    # Try aliases
    aliases = _get_column_aliases()
    if column in aliases:
        resolved = aliases[column]
        if resolved in df.columns:
            return resolved
    
    # If not found, provide helpful error
    available = sorted([col for col in df.columns if not col.startswith('_')])
    raise KeyError(
        f"Column '{column}' not found.\n"
        f"Available columns: {', '.join(available[:20])}"
        f"{'...' if len(available) > 20 else ''}"
    )


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
                        return lambda df, c: df[_resolve_column_name(c, df)] == df[_resolve_column_name(val, df)]
                    if op == "!=":
                        return lambda df, c: df[_resolve_column_name(c, df)] != df[_resolve_column_name(val, df)]
                    if op == ">=":
                        return lambda df, c: df[_resolve_column_name(c, df)] >= df[_resolve_column_name(val, df)]
                    if op == "<=":
                        return lambda df, c: df[_resolve_column_name(c, df)] <= df[_resolve_column_name(val, df)]
                    if op == ">":
                        return lambda df, c: df[_resolve_column_name(c, df)] > df[_resolve_column_name(val, df)]
                    if op == "<":
                        return lambda df, c: df[_resolve_column_name(c, df)] < df[_resolve_column_name(val, df)]

                else:
                    if op in ("==", "="):
                        return lambda df, c, v=val: df[_resolve_column_name(c, df)] == v
                    if op == "!=":
                        return lambda df, c, v=val: df[_resolve_column_name(c, df)] != v
                    if op == ">=":
                        return lambda df, c, v=val: df[_resolve_column_name(c, df)] >= v
                    if op == "<=":
                        return lambda df, c, v=val: df[_resolve_column_name(c, df)] <= v
                    if op == ">":
                        return lambda df, c, v=val: df[_resolve_column_name(c, df)] > v
                    if op == "<":
                        return lambda df, c, v=val: df[_resolve_column_name(c, df)] < v

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
        try:
            # Handle both scalar and column-to-column comparisons
            result = predicate(df, column)
            mask &= result
        except KeyError as e:
            raise KeyError(
                f"Pattern condition failed: {condition}\n"
                f"Error: {str(e)}\n"
                f"Try using aliases like MACD, STOCH_K, RSI, ADX, MOMENTUM, etc."
            )

    return mask.fillna(False)


def _pattern_summary(df, pattern_spec):
    mask = _build_pattern_mask(df, pattern_spec)
    hits = df.loc[mask].copy()
    price_move = (hits["Close"] - hits["Open"]) / hits["Open"] * 100

    if hits.empty:
        return {
            "pattern": pattern_spec,
            "count": 0,
            "coverage_pct": 0,
            "first_occurrence": None,
            "last_occurrence": None,
            "occurrences_per_week": None,
            "occurrences_per_month": None,
            "price_move_mean": None,
            "price_move_median": None,
            "price_move_min": None,
            "price_move_max": None,
            "price_move_std": None,
            "price_move_var": None,
            "p10": None,
            "p25": None,
            "p50": None,
            "p75": None,
            "p90": None,
            "skewness": None,
            "kurtosis": None,
            "bull_count": 0,
            "bear_count": 0,
            "flat_count": 0,
            "bullish_percentage": 0,
            "bearish_percentage": 0,
            "neutral_percentage": 0,
            "dominant_direction": None,
            "directional_confidence": 0,
            "dominance_ratio": None,
            "sample_rows": hits.head(10),
        }

    # Convert UTC to datetime if needed for coverage metrics
    if "UTC" in hits.columns:
        hits["UTC"] = pd.to_datetime(hits["UTC"], errors="coerce")

    coverage_pct = float(len(hits) / len(df) * 100) if len(df) > 0 else 0
    first_occurrence = hits["UTC"].min() if "UTC" in hits.columns else None
    last_occurrence = hits["UTC"].max() if "UTC" in hits.columns else None

    weeks = hits["UTC"].dt.to_period("W").nunique() if "UTC" in hits.columns else 0
    months = hits["UTC"].dt.to_period("M").nunique() if "UTC" in hits.columns else 0
    occurrences_per_week = float(len(hits) / weeks) if weeks else None
    occurrences_per_month = float(len(hits) / months) if months else None

    bull_count = int((price_move > 0).sum())
    bear_count = int((price_move < 0).sum())
    flat_count = int((price_move == 0).sum())
    total = len(price_move)
    bullish_pct = float(bull_count / total * 100) if total else 0
    bearish_pct = float(bear_count / total * 100) if total else 0
    neutral_pct = float(flat_count / total * 100) if total else 0
    dominant_direction = (
        "bullish" if bullish_pct >= bearish_pct and bullish_pct >= neutral_pct else
        "bearish" if bearish_pct >= bullish_pct and bearish_pct >= neutral_pct else
        "neutral"
    )
    dominance_ratio = float(max(bull_count, bear_count, flat_count) / (total - max(bull_count, bear_count, flat_count))) if total - max(bull_count, bear_count, flat_count) > 0 else float("inf")

    result = {
        "pattern": pattern_spec,
        "count": int(total),
        "coverage_pct": coverage_pct,
        "first_occurrence": first_occurrence,
        "last_occurrence": last_occurrence,
        "occurrences_per_week": occurrences_per_week,
        "occurrences_per_month": occurrences_per_month,
        "price_move_mean": float(price_move.mean()),
        "price_move_median": float(price_move.median()),
        "price_move_min": float(price_move.min()),
        "price_move_max": float(price_move.max()),
        "price_move_std": float(price_move.std()),
        "price_move_var": float(price_move.var()),
        "p10": float(price_move.quantile(0.10)),
        "p25": float(price_move.quantile(0.25)),
        "p50": float(price_move.quantile(0.50)),
        "p75": float(price_move.quantile(0.75)),
        "p90": float(price_move.quantile(0.90)),
        "skewness": float(price_move.skew()),
        "kurtosis": float(price_move.kurtosis()),
        "bull_count": bull_count,
        "bear_count": bear_count,
        "flat_count": flat_count,
        "bullish_percentage": bullish_pct,
        "bearish_percentage": bearish_pct,
        "neutral_percentage": neutral_pct,
        "dominant_direction": dominant_direction,
        "directional_confidence": float(max(bullish_pct, bearish_pct, neutral_pct)),
        "dominance_ratio": dominance_ratio,
    }
    
    # Add ATR-normalized move if available
    if "ATR_14" in hits.columns:
        atr_norm = (price_move / hits["ATR_14"]).replace([np.inf, -np.inf], np.nan).dropna()
        if len(atr_norm) > 0:
            result["atr_normalized_mean"] = float(atr_norm.mean())
            result["atr_normalized_std"] = float(atr_norm.std())
        else:
            result["atr_normalized_mean"] = None
            result["atr_normalized_std"] = None
    else:
        result["atr_normalized_mean"] = None
        result["atr_normalized_std"] = None

    # Get all available indicator columns
    indicator_cols = [col for col in hits.columns if col not in ["UTC", "Open", "High", "Low", "Close", "Volume", "Date", "Time"]]
    
    sample_rows = hits[["UTC", "Open", "Close", "High", "Low", "Volume"] + indicator_cols].head(10).copy()
    sample_rows["PriceMovePct"] = (sample_rows["Close"] - sample_rows["Open"]) / sample_rows["Open"] * 100
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

    # Pattern discovery - automatic pattern identification
    with timed_spinner("Discovering indicator patterns"):
        discoverer = pattern_discovery.PatternDiscovery(
            merged,
            min_frequency=max(5, len(merged) // 500),  # More relaxed: 0.2% of data
            min_directional_confidence=55  # Require a stable dominant reaction direction
        )
        discovered_patterns = discoverer.discover(max_patterns=15)
        pattern_discovery_results = discoverer.generate_report_data(top_n=10)
    
    # Pattern summary (user-specified pattern)
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
        "pattern_discovery_results": pattern_discovery_results,
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
        print(f"Dataset Coverage: {summary['coverage_pct']:.2f}%")
        if summary['first_occurrence'] is not None:
            print(f"First Occurrence: {summary['first_occurrence']}")
            print(f"Last Occurrence: {summary['last_occurrence']}")
        if summary['occurrences_per_week'] is not None:
            print(f"Occurrences per week: {summary['occurrences_per_week']:.2f}")
        if summary['occurrences_per_month'] is not None:
            print(f"Occurrences per month: {summary['occurrences_per_month']:.2f}")
        if summary['count'] > 0:
            print(f"Bullish: {summary['bull_count']} ({summary['bullish_percentage']:.2f}%)")
            print(f"Bearish: {summary['bear_count']} ({summary['bearish_percentage']:.2f}%)")
            print(f"Neutral: {summary['flat_count']} ({summary['neutral_percentage']:.2f}%)")
            print(f"Dominant direction: {summary['dominant_direction']}")
            print(f"Directional confidence: {summary['directional_confidence']:.2f}%")
            print(f"Dominance ratio: {summary['dominance_ratio']:.2f}")
            print(f"\n--- MAGNITUDE CONSISTENCY ---")
            print(f"Average price move: {summary['price_move_mean']:.6f}%")
            print(f"Median price move: {summary['price_move_median']:.6f}%")
            print(f"Std dev price move: {summary['price_move_std']:.6f}")
            print(f"Variance: {summary['price_move_var']:.6f}")
            print(f"Min price move: {summary['price_move_min']:.6f}%")
            print(f"Max price move: {summary['price_move_max']:.6f}%")
            print(f"P10: {summary['p10']:.6f}%")
            print(f"P25: {summary['p25']:.6f}%")
            print(f"P50: {summary['p50']:.6f}%")
            print(f"P75: {summary['p75']:.6f}%")
            print(f"P90: {summary['p90']:.6f}%")
            print(f"Skewness: {summary['skewness']:.6f}")
            print(f"Kurtosis: {summary['kurtosis']:.6f}")
            if summary.get('atr_normalized_mean') is not None:
                print(f"ATR-normalized mean move: {summary['atr_normalized_mean']:.6f}")
                print(f"ATR-normalized std dev: {summary['atr_normalized_std']:.6f}")
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

"""Preparation pipeline for enriching raw OHLCV data with indicators and patterns.

This module sits between the data-loading stage and the brute-force analysis
stage. It is responsible for creating the feature-rich payload that the search
engine later uses to generate condition combinations.
"""

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
    compression,
    market_structure,
    volatility_regime,
)


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


def prepare(df):
    """Apply all indicator and pattern modules to a dataframe.

    Purpose:
        Transform the base OHLCV history into the enriched payload that the
        brute-force engine evaluates.

    Inputs:
        df: Raw dataframe with UTC and OHLCV columns.

    Outputs:
        A dataframe with additional indicator and pattern columns.

    Side effects:
        Mutates the dataframe in place through successive module.apply calls.

    Algorithm:
        Indicator modules run first, then pattern modules. Each module adds one
        or more columns that later become available to the condition definitions
        stored in the payload configuration.

    Time complexity:
        O(k * n) where k is the number of modules and n is the number of rows.
    """
    print("[>] Applying indicators...", flush=True)

    for module in indicator_modules:
        print(f"[>] Indicator: {module.__name__}", flush=True)
        df = module.apply(df)

    print("[>] Applying patterns...", flush=True)

    for module in pattern_modules:
        print(f"[>] Pattern: {module.__name__}", flush=True)
        df = module.apply(df)

    return df
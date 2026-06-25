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
    print("[>] Applying indicators...", flush=True)

    for module in indicator_modules:
        print(f"[>] Indicator: {module.__name__}", flush=True)
        df = module.apply(df)

    print("[>] Applying patterns...", flush=True)

    for module in pattern_modules:
        print(f"[>] Pattern: {module.__name__}", flush=True)
        df = module.apply(df)

    return df
from loader import load_all

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

from timeframe import correlation, merge, trend_context, tf_similarity

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


def prepare(df):
    for module in indicator_modules:
        df = module.apply(df)

    for module in pattern_modules:
        df = module.apply(df)

    return df


def main():
    data = load_all()

    for tf, df in data.items():
        data[tf] = prepare(df)

    merged = data["M1"]

    for tf in ["M5", "M15", "H1", "H4", "D1"]:
        merged = merge.merge(merged, data[tf], tf)

    merged = trend_context.apply(merged)

    X = window_builder.build(merged)
    X = X.dropna()

    valid_rows = merged.index[20:][X.index]

    cluster_model.fit(X)
    similar = similarity_search.search(X)

    correlation.analyze(merged)
    tf_similarity.search(merged)

    print(merged.loc[valid_rows[similar], ["UTC", "Close", "COMPRESSION", "VOL_REGIME"]])
    merged.to_csv("XAU_USD_multi_timeframe.csv", index=False)


if __name__ == "__main__":
    main()

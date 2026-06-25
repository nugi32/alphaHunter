def apply(df):
    """
    Calculate MACD (Moving Average Convergence Divergence) with histogram.
    Histogram is MACD line - Signal line and is crucial for divergences.
    """
    combos = [
        (12, 26, 9),
        (5, 35, 5),
        (8, 21, 9),
        (9, 21, 9),
        (12, 34, 9),
    ]

    for fast, slow, signal in combos:
        ema_fast = df["Close"].ewm(
            span=fast,
            adjust=False,
        ).mean()

        ema_slow = df["Close"].ewm(
            span=slow,
            adjust=False,
        ).mean()

        macd = ema_fast - ema_slow
        signal_line = macd.ewm(span=signal, adjust=False).mean()
        histogram = macd - signal_line

        df[f"MACD_{fast}_{slow}"] = macd
        df[f"MACD_SIGNAL_{signal}"] = signal_line
        df[f"MACD_HIST_{fast}_{slow}_{signal}"] = histogram

    return df

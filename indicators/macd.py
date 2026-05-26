def apply(df):
    combos = [
        (12, 26, 9),
        (5, 35, 5),
        (8, 21, 9),
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

        df[f"MACD_{fast}_{slow}"] = macd

        df[f"MACD_SIGNAL_{signal}"] = (
            macd.ewm(
                span=signal,
                adjust=False,
            ).mean()
        )

    return df

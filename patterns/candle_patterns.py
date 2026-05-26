def apply(df):
    body = (df["Close"] - df["Open"]).abs()

    range_ = df["High"] - df["Low"]

    upper = df["High"] - df[["Open", "Close"]].max(axis=1)

    lower = df[["Open", "Close"]].min(axis=1) - df["Low"]

    df["DOJI"] = (body / range_ < 0.1).astype(int)

    df["HAMMER"] = ((lower > body * 2) & (upper < body)).astype(int)

    df["SHOOTING_STAR"] = ((upper > body * 2) & (lower < body)).astype(int)

    prev_open = df["Open"].shift()
    prev_close = df["Close"].shift()

    df["BULL_ENGULF"] = (
        (prev_close < prev_open)
        & (df["Close"] > df["Open"])
        & (df["Close"] > prev_open)
        & (df["Open"] < prev_close)
    ).astype(int)

    df["BEAR_ENGULF"] = (
        (prev_close > prev_open)
        & (df["Close"] < df["Open"])
        & (df["Open"] > prev_close)
        & (df["Close"] < prev_open)
    ).astype(int)

    return df

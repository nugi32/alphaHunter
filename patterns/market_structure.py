def apply(df):
    prev_high = df["High"].shift()
    prev_low = df["Low"].shift()

    df["HH"] = (df["High"] > prev_high).astype(int)
    df["LL"] = (df["Low"] < prev_low).astype(int)

    df["BREAKOUT_UP"] = (
        df["Close"] > df["High"].rolling(20).max().shift()
    ).astype(int)

    df["BREAKOUT_DOWN"] = (
        df["Close"] < df["Low"].rolling(20).min().shift()
    ).astype(int)

    return df

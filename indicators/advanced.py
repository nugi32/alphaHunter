def apply(df):
    high = df["High"].rolling(20).max()
    low = df["Low"].rolling(20).min()

    df["WILLIAMS_R"] = ((high - df["Close"]) / (high - low)) * -100
    df["DONCHIAN_HIGH"] = high
    df["DONCHIAN_LOW"] = low

    atr = df["Close"].diff().abs().rolling(20).mean()
    ema = df["Close"].ewm(span=20, adjust=False).mean()

    df["KELTNER_MID"] = ema
    df["KELTNER_UPPER"] = ema + 2 * atr
    df["KELTNER_LOWER"] = ema - 2 * atr

    return df

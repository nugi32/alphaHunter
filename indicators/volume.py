def apply(df):
    df["VOL_SMA20"] = df["Volume"].rolling(20).mean()

    df["OBV"] = ((df["Close"].diff() > 0) * df["Volume"]).cumsum()

    return df

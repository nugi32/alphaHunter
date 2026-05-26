def apply(df):
    high20 = df["High"].rolling(20).max()
    low20 = df["Low"].rolling(20).min()

    width = (high20 - low20) / df["Close"]

    df["RANGE20"] = width

    df["COMPRESSION"] = (width < width.rolling(100).quantile(0.2)).astype(int)

    return df

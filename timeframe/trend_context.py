def apply(df):
    df["TF_BULL_STACK"] = (
        (df["EMA_20"] > df["EMA_50"])
        & (df["M15_EMA_20"] > df["M15_EMA_50"])
        & (df["H1_EMA_20"] > df["H1_EMA_50"])
    ).astype(int)

    df["TF_BEAR_STACK"] = (
        (df["EMA_20"] < df["EMA_50"])
        & (df["M15_EMA_20"] < df["M15_EMA_50"])
        & (df["H1_EMA_20"] < df["H1_EMA_50"])
    ).astype(int)

    return df

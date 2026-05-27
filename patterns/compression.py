import pandas as pd


def apply(df):
    high20 = df["High"].rolling(20).max()
    low20 = df["Low"].rolling(20).min()

    width = (high20 - low20) / df["Close"]

    # Batch assign columns to avoid DataFrame fragmentation
    comp_cols = pd.concat([
        pd.Series(width, index=df.index, name="RANGE20"),
        pd.Series((width < width.rolling(100).quantile(0.2)).astype(int), index=df.index, name="COMPRESSION"),
    ], axis=1)
    df = pd.concat([df, comp_cols], axis=1)

    return df

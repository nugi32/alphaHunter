import pandas as pd


def apply(df):
    prev_high = df["High"].shift()
    prev_low = df["Low"].shift()

    # Batch assign market structure columns to avoid fragmentation
    structure_cols = pd.concat([
        pd.Series((df["High"] > prev_high).astype(int), index=df.index, name="HH"),
        pd.Series((df["Low"] < prev_low).astype(int), index=df.index, name="LL"),
        pd.Series((df["Close"] > df["High"].rolling(20).max().shift()).astype(int), index=df.index, name="BREAKOUT_UP"),
        pd.Series((df["Close"] < df["Low"].rolling(20).min().shift()).astype(int), index=df.index, name="BREAKOUT_DOWN"),
    ], axis=1)
    df = pd.concat([df, structure_cols], axis=1)

    return df

import pandas as pd

PERIODS = [7, 14, 21]


def apply(df):
    tr = pd.concat(
        [
            df["High"] - df["Low"],
            (df["High"] - df["Close"].shift()).abs(),
            (df["Low"] - df["Close"].shift()).abs(),
        ],
        axis=1,
    ).max(axis=1)

    for p in PERIODS:
        df[f"ATR_{p}"] = tr.rolling(p).mean()

    return df

import pandas as pd

PERIODS = [5, 9, 10, 14, 20, 21, 50, 100, 200]


def apply(df):
    for p in PERIODS:
        df[f"SMA_{p}"] = df["Close"].rolling(p).mean()

        df[f"EMA_{p}"] = df["Close"].ewm(
            span=p,
            adjust=False,
        ).mean()

        weights = range(1, p + 1)

        df[f"WMA_{p}"] = (
            df["Close"]
            .rolling(p)
            .apply(
                lambda x: (x * weights).sum() / sum(weights),
                raw=True,
            )
        )

    return df

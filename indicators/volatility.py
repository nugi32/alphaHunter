import pandas as pd


def apply(df):
    returns = df["Close"].pct_change()
    extra = {}

    for p in [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        extra[f"VOLATILITY_{p}"] = returns.rolling(p).std()

    return pd.concat([df, pd.DataFrame(extra, index=df.index)], axis=1)

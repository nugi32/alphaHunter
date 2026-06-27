import pandas as pd


def apply(df):
    series = {}
    for p in [5, 10, 20]:
        series[f"MOM_{p}"] = df["Close"] - df["Close"].shift(p)
        series[f"ROC_{p}"] = (df["Close"] / df["Close"].shift(p) - 1) * 100

    return pd.concat([df, pd.DataFrame(series, index=df.index)], axis=1)

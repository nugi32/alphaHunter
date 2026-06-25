import numpy as np
import pandas as pd

PERIODS = [5, 8, 9, 10, 13, 14, 20, 21, 34, 50, 100, 200]


def _wma(series, period):
    values = series.to_numpy(dtype=float)

    if period <= 0:
        raise ValueError("period must be positive")

    if len(values) < period:
        return pd.Series(np.full(len(values), np.nan), index=series.index)

    weights = np.arange(1, period + 1, dtype=float)[::-1]
    denom = weights.sum()

    conv = np.convolve(values, weights, mode="valid") / denom

    out = np.full(len(values), np.nan)
    out[period - 1 :] = conv

    return pd.Series(out, index=series.index)


def apply(df):
    for p in PERIODS:
        df[f"SMA_{p}"] = df["Close"].rolling(p).mean()

        df[f"EMA_{p}"] = df["Close"].ewm(
            span=p,
            adjust=False,
        ).mean()

        df[f"WMA_{p}"] = _wma(df["Close"], p)

    return df

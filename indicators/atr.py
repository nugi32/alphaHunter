import pandas as pd
import numpy as np

PERIODS = [5, 8, 13, 14, 21, 34]


def _wilders_moving_average(series, period):
    """
    Calculate Wilder's moving average (also called Wilder's smoothing).
    Used for ATR calculations per Wilder's original method.
    """
    result = pd.Series(0.0, index=series.index)
    
    # First value is simple average of first period values
    result.iloc[period - 1] = series.iloc[:period].mean()
    
    # Subsequent values use Wilder's smoothing formula
    for i in range(period, len(series)):
        result.iloc[i] = (result.iloc[i - 1] * (period - 1) + series.iloc[i]) / period
    
    return result


def apply(df):
    # Calculate True Range
    tr = pd.concat(
        [
            df["High"] - df["Low"],
            (df["High"] - df["Close"].shift()).abs(),
            (df["Low"] - df["Close"].shift()).abs(),
        ],
        axis=1,
    ).max(axis=1)

    for p in PERIODS:
        df[f"ATR_{p}"] = _wilders_moving_average(tr, p)

    return df

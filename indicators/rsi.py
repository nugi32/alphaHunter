import pandas as pd
import numpy as np


def _wilders_moving_average(series, period):
    """
    Calculate Wilder's moving average (Wilder's smoothing).
    Used for RSI calculations per Wilder's original method.
    """
    result = pd.Series(0.0, index=series.index, dtype=float)
    
    # First value is simple average of first period values
    result.iloc[period - 1] = series.iloc[:period].mean()
    
    # Subsequent values use Wilder's smoothing formula
    for i in range(period, len(series)):
        result.iloc[i] = (result.iloc[i - 1] * (period - 1) + series.iloc[i]) / period
    
    return result


def apply(df):
    delta = df["Close"].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    for p in [7, 13, 14, 21, 34]:
        # Use Wilder's smoothing instead of simple moving average
        avg_gain = _wilders_moving_average(gain, p)
        avg_loss = _wilders_moving_average(loss, p)

        rs = avg_gain / avg_loss.replace(0, np.nan)

        df[f"RSI_{p}"] = 100 - (100 / (1 + rs))

    return df

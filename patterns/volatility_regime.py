import pandas as pd
import numpy as np


def apply(df):
    """
    Classify volatility regime into Low (1), Medium (2), High (3).
    Based on 30-period rolling standard deviation of returns.
    """
    returns = df["Close"].pct_change()

    vol = returns.rolling(30).std()

    # Use quantile-based regime classification
    # Low: bottom 33%, Medium: middle 34%, High: top 33%
    q1 = vol.quantile(0.33)
    q2 = vol.quantile(0.66)

    # Assign regimes
    vol_regime = pd.Series(2, index=df.index, dtype=int)  # Default to medium
    vol_regime[vol < q1] = 1  # Low
    vol_regime[vol > q2] = 3  # High
    
    # Batch assign columns to avoid DataFrame fragmentation
    vol_cols = pd.concat([
        pd.Series(vol, index=df.index, name="VOL30"),
        pd.Series(vol_regime, index=df.index, name="VOL_REGIME"),
    ], axis=1)
    df = pd.concat([df, vol_cols], axis=1)

    return df

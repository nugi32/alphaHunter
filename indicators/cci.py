import pandas as pd
import numpy as np


def apply(df):
    """
    Calculate Commodity Channel Index (CCI).
    CCI measures deviation of price from average price.
    Typical value: ±100 for normal range.
    """
    tp = (df["High"] + df["Low"] + df["Close"]) / 3

    for p in [9, 14, 20, 21]:
        sma = tp.rolling(p).mean()
        mad = (tp - sma).abs().rolling(p).mean()

        # Avoid division by zero: if MAD is 0, CCI is 0
        cci = pd.Series(0.0, index=df.index)
        mask = mad != 0
        cci[mask] = (tp[mask] - sma[mask]) / (0.015 * mad[mask])
        cci[~mask] = 0

        df[f"CCI_{p}"] = cci

    return df

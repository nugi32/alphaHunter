import pandas as pd
import numpy as np

LEVELS = [0.236, 0.382, 0.5, 0.618, 0.786]


def apply(df):
    """
    Calculate Fibonacci retracement levels from recent swing high/low.
    Uses 100-period lookback to find significant swings.
    """
    # Find swing highs and lows over lookback period
    lookback = 100
    
    high_100 = df["High"].rolling(lookback).max()
    low_100 = df["Low"].rolling(lookback).min()
    
    diff = high_100 - low_100

    # Calculate retracement levels from swing high
    extra = {}
    for level in LEVELS:
        # Levels are measured down from recent high
        extra[f"FIB_{level}"] = high_100 - diff * level

    # Also provide the swing high and low reference
    extra["FIB_HIGH"] = high_100
    extra["FIB_LOW"] = low_100

    return pd.concat([df, pd.DataFrame(extra, index=df.index)], axis=1)

import pandas as pd
import numpy as np


def apply(df):
    """
    Detect recent swing highs and lows (support/resistance levels).
    Swing High: local maximum with lookback period
    Swing Low: local minimum with lookback period
    """
    lookback = 5  # Periods to check on each side
    
    swing_high = pd.Series(0.0, index=df.index)
    swing_low = pd.Series(0.0, index=df.index)
    
    for i in range(lookback, len(df) - lookback):
        # Check if current high is highest in window
        if df["High"].iloc[i] == df["High"].iloc[i-lookback:i+lookback+1].max():
            swing_high.iloc[i] = df["High"].iloc[i]
        
        # Check if current low is lowest in window
        if df["Low"].iloc[i] == df["Low"].iloc[i-lookback:i+lookback+1].min():
            swing_low.iloc[i] = df["Low"].iloc[i]
    
    # Batch assign columns to avoid DataFrame fragmentation
    result_cols = pd.concat([
        pd.Series(swing_high, index=df.index, name="SWING_HIGH"),
        pd.Series(swing_low, index=df.index, name="SWING_LOW"),
    ], axis=1)
    
    df = pd.concat([df, result_cols], axis=1)

    return df

import pandas as pd
import numpy as np


def apply(df):
    """
    Bollinger Bands and Keltner Channel Squeeze indicator.
    Squeeze occurs when BB is inside KC, indicating low volatility and potential breakout.
    """
    # Bollinger Bands (20, 2)
    sma20 = df["Close"].rolling(20).mean()
    std20 = df["Close"].rolling(20).std()
    bb_upper = sma20 + 2 * std20
    bb_lower = sma20 - 2 * std20

    # Keltner Channel (20, 2 ATR)
    tr = pd.concat([
        df["High"] - df["Low"],
        (df["High"] - df["Close"].shift()).abs(),
        (df["Low"] - df["Close"].shift()).abs(),
    ], axis=1).max(axis=1)
    atr = tr.rolling(20).mean()
    
    ema20 = df["Close"].ewm(span=20, adjust=False).mean()
    kc_upper = ema20 + 2 * atr
    kc_lower = ema20 - 2 * atr

    # Squeeze: BB inside KC
    squeeze = (bb_upper < kc_upper) & (bb_lower > kc_lower)
    
    # Batch assign columns to avoid DataFrame fragmentation
    result_cols = pd.concat([
        pd.Series(squeeze.astype(int), index=df.index, name="SQUEEZE"),
        pd.Series(bb_upper, index=df.index, name="BB_UPPER"),
        pd.Series(bb_lower, index=df.index, name="BB_LOWER"),
        pd.Series(kc_upper, index=df.index, name="KC_UPPER"),
        pd.Series(kc_lower, index=df.index, name="KC_LOWER"),
    ], axis=1)
    
    df = pd.concat([df, result_cols], axis=1)

    return df

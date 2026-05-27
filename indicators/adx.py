import pandas as pd
import numpy as np


def apply(df):
    """
    Calculate ADX (Average Directional Index) using Wilder's smoothing method.
    ADX measures trend strength from 0-100, independent of direction.
    """
    period = 14
    
    # Calculate directional movements
    up_move = df["High"].diff()
    down_move = -df["Low"].diff()
    
    # Initialize positive and negative directional movements
    pos_dm = np.where((up_move > down_move) & (up_move > 0), up_move, 0)
    neg_dm = np.where((down_move > up_move) & (down_move > 0), down_move, 0)
    
    # Calculate true range
    tr = pd.concat([
        df["High"] - df["Low"],
        (df["High"] - df["Close"].shift()).abs(),
        (df["Low"] - df["Close"].shift()).abs(),
    ], axis=1).max(axis=1)
    
    # Initialize Wilder's smoothed values
    tr_smooth = pd.Series(0.0, index=df.index)
    pos_dm_smooth = pd.Series(0.0, index=df.index)
    neg_dm_smooth = pd.Series(0.0, index=df.index)
    
    # First smoothed values (simple sum of first 14 periods)
    tr_smooth.iloc[period - 1] = tr.iloc[:period].sum()
    pos_dm_smooth.iloc[period - 1] = pos_dm[:period].sum()
    neg_dm_smooth.iloc[period - 1] = neg_dm[:period].sum()
    
    # Wilder's smoothing for subsequent values
    for i in range(period, len(df)):
        tr_smooth.iloc[i] = tr_smooth.iloc[i - 1] - tr_smooth.iloc[i - 1] / period + tr.iloc[i]
        pos_dm_smooth.iloc[i] = pos_dm_smooth.iloc[i - 1] - pos_dm_smooth.iloc[i - 1] / period + pos_dm[i]
        neg_dm_smooth.iloc[i] = neg_dm_smooth.iloc[i - 1] - neg_dm_smooth.iloc[i - 1] / period + neg_dm[i]
    
    # Calculate directional indicators
    pos_di = 100 * (pos_dm_smooth / tr_smooth.replace(0, np.nan))
    neg_di = 100 * (neg_dm_smooth / tr_smooth.replace(0, np.nan))
    
    # Calculate DX
    dx = 100 * np.abs(pos_di - neg_di) / (pos_di + neg_di).replace(0, np.nan)
    
    # Smooth DX using Wilder's method to get ADX
    adx = pd.Series(0.0, index=df.index)
    
    # First ADX value (simple average of first 14 DX values)
    adx.iloc[2 * period - 2] = dx.iloc[period:2 * period].mean()
    
    # Subsequent ADX values use Wilder's smoothing
    for i in range(2 * period - 1, len(df)):
        adx.iloc[i] = (adx.iloc[i - 1] * (period - 1) + dx.iloc[i]) / period
    
    df["ADX_14"] = adx
    df["DI_PLUS_14"] = pos_di
    df["DI_MINUS_14"] = neg_di
    
    return df

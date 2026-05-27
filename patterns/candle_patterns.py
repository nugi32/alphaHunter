import pandas as pd


def apply(df):
    """
    Calculate candlestick patterns commonly used in technical analysis.
    """
    body = (df["Close"] - df["Open"]).abs()
    range_ = df["High"] - df["Low"]
    upper = df["High"] - df[["Open", "Close"]].max(axis=1)
    lower = df[["Open", "Close"]].min(axis=1) - df["Low"]

    # Single candle patterns - batch assign to avoid fragmentation
    candle_cols = pd.concat([
        pd.Series((body / range_ < 0.1).astype(int), index=df.index, name="DOJI"),
        pd.Series(((lower > body * 2) & (upper < body)).astype(int), index=df.index, name="HAMMER"),
        pd.Series(((upper > body * 2) & (lower < body)).astype(int), index=df.index, name="SHOOTING_STAR"),
        pd.Series((range_ > df["Close"].rolling(20).mean() * 1.5).astype(int), index=df.index, name="LONG_CANDLE"),
        pd.Series((range_ < df["Close"].rolling(20).mean() * 0.5).astype(int), index=df.index, name="SMALL_CANDLE"),
    ], axis=1)
    df = pd.concat([df, candle_cols], axis=1)

    # Two candle patterns
    prev_open = df["Open"].shift()
    prev_close = df["Close"].shift()
    prev_high = df["High"].shift()
    prev_low = df["Low"].shift()

    # Bullish engulfing: previous bearish candle, current bullish candle engulfs it
    bull_engulf = (
        (prev_close < prev_open)
        & (df["Close"] > df["Open"])
        & (df["Close"] > prev_open)
        & (df["Open"] < prev_close)
    ).astype(int)

    # Bearish engulfing: previous bullish candle, current bearish candle engulfs it
    bear_engulf = (
        (prev_close > prev_open)
        & (df["Close"] < df["Open"])
        & (df["Open"] > prev_close)
        & (df["Close"] < prev_open)
    ).astype(int)
    
    # Harami (reversal): small candle inside previous larger candle
    bull_harami = (
        (prev_close < prev_open)
        & (df["Close"] > df["Open"])
        & (df["Close"] < prev_open)
        & (df["Open"] > prev_close)
        & (body < (prev_open - prev_close))
    ).astype(int)

    bear_harami = (
        (prev_close > prev_open)
        & (df["Close"] < df["Open"])
        & (df["Close"] > prev_open)
        & (df["Open"] < prev_close)
        & (body < (prev_close - prev_open))
    ).astype(int)
    
    # Batch assign two-candle patterns to avoid fragmentation
    engulf_cols = pd.concat([
        pd.Series(bull_engulf, index=df.index, name="BULL_ENGULF"),
        pd.Series(bear_engulf, index=df.index, name="BEAR_ENGULF"),
        pd.Series(bull_harami, index=df.index, name="BULL_HARAMI"),
        pd.Series(bear_harami, index=df.index, name="BEAR_HARAMI"),
    ], axis=1)
    df = pd.concat([df, engulf_cols], axis=1)

    return df

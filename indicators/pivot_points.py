def apply(df):
    """
    Calculate standard pivot points (S2, S1, PP, R1, R2).
    Based on the previous day's High, Low, Close.
    """
    # Previous day's OHLC (shift by 1)
    prev_high = df["High"].shift(1)
    prev_low = df["Low"].shift(1)
    prev_close = df["Close"].shift(1)

    # Pivot Point
    pivot = (prev_high + prev_low + prev_close) / 3

    # Resistance and Support levels
    r1 = 2 * pivot - prev_low
    s1 = 2 * pivot - prev_high
    r2 = pivot + (prev_high - prev_low)
    s2 = pivot - (prev_high - prev_low)

    df["PIVOT"] = pivot
    df["R1"] = r1
    df["R2"] = r2
    df["S1"] = s1
    df["S2"] = s2

    return df

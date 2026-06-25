def apply(df):
    """
    Calculate Stochastic Oscillator with properly smoothed %K.
    Standard: Fast Stochastic uses raw %K
    Slow: Smooths %K first, then applies %D smoothing
    """
    for p in [5, 9, 14, 21]:
        low = df["Low"].rolling(p).min()
        high = df["High"].rolling(p).max()

        # Fast Stochastic %K (raw)
        k_raw = ((df["Close"] - low) / (high - low)) * 100
        
        # Slow Stochastic %K (smoothed with 3-period MA)
        k_slow = k_raw.rolling(3).mean()
        
        # %D is 3-period MA of %K
        d = k_slow.rolling(3).mean()

        df[f"STO_K_{p}"] = k_slow
        df[f"STO_D_{p}"] = d
        df[f"STO_K_RAW_{p}"] = k_raw

    return df

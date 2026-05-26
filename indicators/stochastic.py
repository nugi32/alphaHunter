def apply(df):
    for p in [14, 21]:
        low = df["Low"].rolling(p).min()
        high = df["High"].rolling(p).max()

        k = ((df["Close"] - low) / (high - low)) * 100
        d = k.rolling(3).mean()

        df[f"STO_K_{p}"] = k
        df[f"STO_D_{p}"] = d

    return df

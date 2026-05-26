def apply(df):
    tp = (df["High"] + df["Low"] + df["Close"]) / 3

    for p in [14, 20]:
        sma = tp.rolling(p).mean()
        mad = (tp - sma).abs().rolling(p).mean()

        df[f"CCI_{p}"] = (tp - sma) / (0.015 * mad)

    return df

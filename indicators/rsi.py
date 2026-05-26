def apply(df):
    delta = df["Close"].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    for p in [7, 14, 21]:
        avg_gain = gain.rolling(p).mean()
        avg_loss = loss.rolling(p).mean()

        rs = avg_gain / avg_loss.replace(0, float("nan"))

        df[f"RSI_{p}"] = 100 - (100 / (1 + rs))

    return df

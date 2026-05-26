PERIODS = [20, 50]
MULTI = [2, 3]


def apply(df):
    for p in PERIODS:
        sma = df["Close"].rolling(p).mean()
        std = df["Close"].rolling(p).std()

        for m in MULTI:
            df[f"BB_UPPER_{p}_{m}"] = sma + std * m
            df[f"BB_LOWER_{p}_{m}"] = sma - std * m

    return df

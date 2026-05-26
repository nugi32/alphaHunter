LEVELS = [0.236, 0.382, 0.5, 0.618]


def apply(df):
    high = df["High"].rolling(100).max()
    low = df["Low"].rolling(100).min()

    diff = high - low

    for level in LEVELS:
        df[f"FIB_{level}"] = high - diff * level

    return df

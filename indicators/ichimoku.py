def apply(df):
    df["TENKAN"] = (
        df["High"].rolling(9).max() + df["Low"].rolling(9).min()
    ) / 2

    df["KIJUN"] = (
        df["High"].rolling(26).max() + df["Low"].rolling(26).min()
    ) / 2

    return df

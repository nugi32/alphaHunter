def apply(df):
    df["ADX_14"] = (df["High"] - df["Low"]).rolling(14).mean()
    return df

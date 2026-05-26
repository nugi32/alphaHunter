def apply(df):
    for p in [5, 10, 20]:
        df[f"MOM_{p}"] = df["Close"] - df["Close"].shift(p)
        df[f"ROC_{p}"] = (df["Close"] / df["Close"].shift(p) - 1) * 100

    return df

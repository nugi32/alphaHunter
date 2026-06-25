def apply(df):
    returns = df["Close"].pct_change()

    for p in [10, 20, 50]:
        df[f"VOLATILITY_{p}"] = returns.rolling(p).std()

    return df

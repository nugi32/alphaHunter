def apply(df):
    returns = df["Close"].pct_change()

    vol = returns.rolling(30).std()

    df["VOL30"] = vol

    q1 = vol.quantile(0.33)
    q2 = vol.quantile(0.66)

    df["VOL_REGIME"] = 0

    df.loc[vol < q1, "VOL_REGIME"] = 1
    df.loc[vol > q2, "VOL_REGIME"] = 3

    return df

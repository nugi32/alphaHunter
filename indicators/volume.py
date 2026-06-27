import pandas as pd


def apply(df):
    extra = {
        "VOL_SMA20": df["Volume"].rolling(20).mean(),
    }

    # OBV: Add volume on up days, subtract on down days
    # Handle the first row specially
    obv = pd.Series(0.0, index=df.index)
    obv.iloc[0] = 0

    for i in range(1, len(df)):
        if df["Close"].iloc[i] > df["Close"].iloc[i - 1]:
            obv.iloc[i] = obv.iloc[i - 1] + df["Volume"].iloc[i]
        elif df["Close"].iloc[i] < df["Close"].iloc[i - 1]:
            obv.iloc[i] = obv.iloc[i - 1] - df["Volume"].iloc[i]
        else:
            obv.iloc[i] = obv.iloc[i - 1]

    extra["OBV"] = obv

    return pd.concat([df, pd.DataFrame(extra, index=df.index)], axis=1)

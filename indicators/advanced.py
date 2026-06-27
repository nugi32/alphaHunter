import pandas as pd


def apply(df):
    high = df["High"].rolling(20).max()
    low = df["Low"].rolling(20).min()

    atr = df["Close"].diff().abs().rolling(20).mean()
    ema = df["Close"].ewm(span=20, adjust=False).mean()

    extra = {
        "WILLIAMS_R": ((high - df["Close"]) / (high - low)) * -100,
        "DONCHIAN_HIGH": high,
        "DONCHIAN_LOW": low,
        "KELTNER_MID": ema,
        "KELTNER_UPPER": ema + 2 * atr,
        "KELTNER_LOWER": ema - 2 * atr,
    }

    return pd.concat([df, pd.DataFrame(extra, index=df.index)], axis=1)

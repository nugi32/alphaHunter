import pandas as pd

FEATURES = [
    "EMA_20",
    "EMA_50",
    "RSI_14",
    "VOL30",
    "COMPRESSION",
    "DOJI",
    "HAMMER",
]


def build(df, window=20):
    rows = []

    for i in range(window, len(df)):
        values = []

        for col in FEATURES:
            values.extend(df[col].iloc[i - window : i].tolist())

        rows.append(values)

    return pd.DataFrame(rows)

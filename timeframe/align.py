import pandas as pd


def align_to_base(base, other):
    return pd.merge_asof(base, other, on="UTC", direction="backward")


def ensure_datetime(df):
    df = df.copy()
    df["UTC"] = pd.to_datetime(df["UTC"])
    return df.sort_values("UTC").reset_index(drop=True)

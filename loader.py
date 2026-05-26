import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

FILES = {
    "M1": "XAUUSD1.csv",
    "M5": "XAUUSD5.csv",
    "M15": "XAUUSD15.csv",
    "H1": "XAUUSD60.csv",
    "H4": "XAUUSD240.csv",
    "D1": "XAUUSD1440.csv",
    "W1": "XAUUSD10080.csv",
    "MN1": "XAUUSD43200.csv",
}


def _resolve_path(tf):
    candidates = [
        BASE_DIR / "data" / f"XAUUSD_{tf}.csv",
        BASE_DIR / "data" / "XAUUSD" / FILES[tf],
    ]

    for path in candidates:
        if path.exists():
            return path

    raise FileNotFoundError(f"Cannot find data file for {tf}: {candidates}")


def _load_tf(tf):
    path = _resolve_path(tf)

    df = pd.read_csv(path, header=None, names=["Date", "Time", "Open", "High", "Low", "Close", "Volume"])

    df["UTC"] = pd.to_datetime(
        df["Date"].astype(str) + " " + df["Time"].astype(str),
        format="%Y.%m.%d %H:%M",
        errors="coerce",
    )

    df = df.dropna(subset=["UTC"]).copy()
    df = df.sort_values("UTC").reset_index(drop=True)

    return df[["UTC", "Open", "High", "Low", "Close", "Volume"]]


def load_all():
    data = {tf: _load_tf(tf) for tf in FILES}
    return data


def loadPrice():
    return load_all()
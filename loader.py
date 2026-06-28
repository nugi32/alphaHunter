"""Market-data loading helpers.

This module resolves the local CSV files that back the analysis pipeline and
converts the raw instrument data into the OHLCV dataframe shape expected by the
rest of the project. It exists at the very start of the execution flow and is
used by the prepare and run commands to obtain the raw market history.
"""

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
    """Resolve the on-disk CSV path for a timeframe.

    Purpose:
        Locate the correct instrument history file even when the repository uses
        different directory layouts for different timeframes.

    Inputs:
        tf: The timeframe key, such as H1 or D1.

    Outputs:
        A Path object pointing to an existing CSV file.

    Side effects:
        None.

    Assumptions:
        The repository contains one of the expected data files.
    """
    candidates = [
        BASE_DIR / "data" / f"XAUUSD_{tf}.csv",
        BASE_DIR / "data" / "XAUUSD" / FILES[tf],
    ]

    for path in candidates:
        if path.exists():
            return path

    raise FileNotFoundError(f"Cannot find data file for {tf}: {candidates}")


def _load_tf(tf, limit=None):
    """Load a single timeframe as a cleaned OHLCV dataframe.

    Purpose:
        Parse the raw CSV format used by the project into a standard pandas
        dataframe with UTC timestamps and OHLCV columns.

    Inputs:
        tf: Timeframe identifier.
        limit: Optional maximum number of rows to return. When provided, the
            loader reads in chunks and keeps only the most recent rows.

    Outputs:
        A dataframe with UTC, Open, High, Low, Close, and Volume columns.

    Algorithm:
        The function uses chunked CSV parsing when a limit is requested to avoid
        loading the full file into memory at once. It then converts the Date/Time
        columns into a datetime index and removes invalid rows.

    Time complexity:
        O(n) in the number of rows parsed.

    Memory complexity:
        O(limit) when limit is used; otherwise O(n) for the whole dataframe.
    """
    path = _resolve_path(tf)

    if limit is None:
        df = pd.read_csv(path, header=None, names=["Date", "Time", "Open", "High", "Low", "Close", "Volume"])

        df["UTC"] = pd.to_datetime(
            df["Date"].astype(str) + " " + df["Time"].astype(str),
            format="%Y.%m.%d %H:%M",
            errors="coerce",
        )

        df = df.dropna(subset=["UTC"]).copy()
        df = df.sort_values("UTC").reset_index(drop=True)

        return df[["UTC", "Open", "High", "Low", "Close", "Volume"]]

    tail = None

    for chunk in pd.read_csv(path, header=None, names=["Date", "Time", "Open", "High", "Low", "Close", "Volume"], chunksize=500000):
        chunk["UTC"] = pd.to_datetime(
            chunk["Date"].astype(str) + " " + chunk["Time"].astype(str),
            format="%Y.%m.%d %H:%M",
            errors="coerce",
        )

        chunk = chunk.dropna(subset=["UTC"]).copy()

        if chunk.empty:
            continue

        if tail is None:
            tail = chunk
        else:
            tail = pd.concat([tail, chunk], ignore_index=True)

        if len(tail) > limit:
            tail = tail.tail(limit)

    if tail is None:
        return pd.DataFrame(columns=["UTC", "Open", "High", "Low", "Close", "Volume"])

    tail = tail.sort_values("UTC").reset_index(drop=True)

    return tail[["UTC", "Open", "High", "Low", "Close", "Volume"]]


def load_tf(tf, limit=None):
    """Public wrapper for loading a single timeframe with validation."""
    if tf not in FILES:
        raise ValueError(f"Unsupported timeframe: {tf}. Allowed: {sorted(FILES)}")

    return _load_tf(tf, limit=limit)


def load_all():
    """Load every supported timeframe into a dictionary."""
    data = {tf: _load_tf(tf) for tf in FILES}
    return data


def loadPrice():
    """Backward-compatible alias for loading all timeframe data."""
    return load_all()
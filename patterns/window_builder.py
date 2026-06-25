import pandas as pd
import numpy as np

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
    n_rows = len(df) - window
    n_features = len(FEATURES)
    
    # Create output array with pre-allocated memory
    output = np.zeros((n_rows, n_features * window), dtype=np.float64)
    
    # Fill array efficiently using numpy operations
    for feat_idx, col in enumerate(FEATURES):
        col_data = df[col].values
        for i in range(n_rows):
            output[i, feat_idx * window:(feat_idx + 1) * window] = col_data[i:i + window]
    
    return pd.DataFrame(output)

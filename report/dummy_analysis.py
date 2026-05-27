import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

df = pd.DataFrame({
    "UTC": pd.date_range("2024-01-01", periods=n, freq="H"),
    "Open": np.random.normal(2500, 40, n),
    "Close": np.random.normal(2500, 40, n),
    "High": np.random.normal(2520, 40, n),
    "Low": np.random.normal(2480, 40, n),
    "Volume": np.random.randint(10, 500, n),

    "RSI_14": np.random.uniform(50, 95, n),
    "ADX_14": np.random.uniform(10, 45, n),
    "CCI_14": np.random.normal(100, 120, n),

    "VOL_REGIME": np.random.choice([0, 1, 2, 3], n),

    "DOJI": np.random.choice([0, 1], n, p=[0.9, 0.1]),
    "HAMMER": np.random.choice([0, 1], n, p=[0.95, 0.05]),

    "PriceMove": np.random.normal(1.0, 3.0, n),
})

df["Bullish"] = df["Close"] > df["Open"]

# filter seperti real command:
pattern_df = df[df["RSI_14"] > 70]

print(pattern_df.head())

# optional save
pattern_df.to_csv("pattern_dummy.csv", index=False)
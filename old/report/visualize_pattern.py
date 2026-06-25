import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("pattern_dummy.csv", parse_dates=["UTC"])

plt.style.use("default")

# ======================================
# 1. Bullish vs Bearish
# ======================================

counts = [
    (df["PriceMove"] > 0).sum(),
    (df["PriceMove"] < 0).sum(),
    (df["PriceMove"] == 0).sum(),
]

labels = ["Bullish", "Bearish", "Flat"]

plt.figure(figsize=(6,4))
plt.bar(labels, counts)
plt.title("Pattern Outcome Distribution")
plt.ylabel("Occurrences")
plt.show()


# ======================================
# 2. Histogram PriceMove
# ======================================

plt.figure(figsize=(8,4))
plt.hist(df["PriceMove"], bins=40)
plt.axvline(df["PriceMove"].mean(), linestyle="--", label="Mean")
plt.axvline(df["PriceMove"].median(), linestyle=":", label="Median")
plt.legend()
plt.title("PriceMove Distribution")
plt.show()


# ======================================
# 3. RSI vs PriceMove
# ======================================

plt.figure(figsize=(8,5))
plt.scatter(df["RSI_14"], df["PriceMove"], alpha=0.4)
plt.axhline(0, linestyle="--")
plt.title("RSI_14 vs PriceMove")
plt.xlabel("RSI_14")
plt.ylabel("PriceMove")
plt.show()


# ======================================
# 4. Volume regime vs average move
# ======================================

grouped = df.groupby("VOL_REGIME")["PriceMove"].mean()

plt.figure(figsize=(6,4))
grouped.plot(kind="bar")
plt.title("Average PriceMove by Volatility Regime")
plt.ylabel("Avg Move")
plt.show()


# ======================================
# 5. Time trend
# ======================================

daily = df.set_index("UTC")["PriceMove"].resample("D").mean()

plt.figure(figsize=(10,4))
daily.plot()
plt.axhline(0, linestyle="--")
plt.title("Daily Average PriceMove")
plt.ylabel("Move")
plt.show()
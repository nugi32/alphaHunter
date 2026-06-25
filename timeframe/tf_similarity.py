from sklearn.metrics.pairwise import cosine_similarity

FEATURES = [
    "EMA_20",
    "EMA_50",
    "COMPRESSION",
    "M15_EMA_20",
    "M15_RSI_14",
    "H1_EMA_50",
    "H4_VOL30",
]


def search(df):
    X = df[FEATURES].fillna(0)
    current = X.iloc[-1:]

    sim = cosine_similarity(X, current).flatten()
    idx = sim.argsort()[-10:]

    print(df.iloc[idx][["UTC", "Close"]])

    return idx

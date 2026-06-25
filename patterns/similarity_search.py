from sklearn.metrics.pairwise import euclidean_distances


def search(X):
    current = X.iloc[-1:]

    dist = euclidean_distances(X, current).flatten()
    idx = dist.argsort()[:10]

    return idx

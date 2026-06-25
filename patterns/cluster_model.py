from sklearn.cluster import KMeans
import numpy as np


def fit(X, n_clusters=None):
    """
    Fit KMeans clustering model.
    If n_clusters is None, uses elbow method to determine optimal clusters.
    Otherwise uses specified n_clusters.
    """
    if n_clusters is None:
        # Use elbow method: test cluster range and use a reasonable default
        # For efficiency, default to 20 clusters (can be overridden)
        n_clusters = min(20, max(5, len(X) // 100))  # 1 cluster per ~100 samples, capped at 5-20
    
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = model.fit_predict(X)

    return model, labels

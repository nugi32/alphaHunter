from sklearn.cluster import KMeans


def fit(X):
    model = KMeans(n_clusters=20, random_state=42)
    labels = model.fit_predict(X)

    return model, labels

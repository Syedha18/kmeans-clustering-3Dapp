from sklearn.cluster import KMeans

def run_kmeans(X, k):
    model = KMeans(n_clusters=k, random_state=42)
    clusters = model.fit_predict(X)
    return clusters
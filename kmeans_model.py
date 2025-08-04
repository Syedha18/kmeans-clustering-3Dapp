from sklearn.cluster import KMeans

def run_kmeans(X, k=3):
    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(X)
    return clusters
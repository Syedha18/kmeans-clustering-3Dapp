from sklearn.cluster import KMeans

def run_kmeans(data, n_clusters):
    # ⿡ Initialize KMeans model
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)

    # ⿢ Fit the model and predict clusters
    clusters = kmeans.fit_predict(data)

    # ⿣ Return the cluster labels
    return clusters
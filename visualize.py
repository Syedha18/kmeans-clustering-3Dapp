import plotly.express as px

def plot_clusters(X, clusters):
    fig = px.scatter_3d(
        X,
        x=X.columns[0],
        y=X.columns[1],
        z=X.columns[2],
        color=clusters.astype(str),
        title="3D K-Means Clustering",
        labels={'color': 'Cluster'}
    )
    fig.update_traces(marker=dict(size=5))
    return fig
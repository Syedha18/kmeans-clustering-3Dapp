import plotly.express as px
import pandas as pd

def plot_clusters(X, clusters):
    data = X.copy()
    data['Cluster'] = clusters
    fig = px.scatter_3d(
        data,
        x=data.columns[0],
        y=data.columns[1],
        z=data.columns[2],
        color='Cluster',
        symbol='Cluster',
        title="K-Means 3D Clustering",
        opacity=0.8
    )
    fig.update_traces(marker=dict(size=6))
    return fig
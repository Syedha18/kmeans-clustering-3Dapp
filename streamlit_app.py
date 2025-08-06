import streamlit as st
from data_loader import load_data
from kmeans_model import run_kmeans
from visualize import plot_clusters
import pandas as pd

st.set_page_config(page_title="K-Means 3D Clustering", page_icon="📊", layout="wide")

st.title("K-Means 3D Clustering")
st.write("Upload your CSV file, preprocess it, choose clusters, and visualize them in 3D!")

with st.sidebar:
    st.header("K-Means Clustering")
    st.markdown("""
    ### What is K-Means?
    K-Means is an *unsupervised machine learning algorithm* used to group similar data points into k clusters.  
    It is widely used in *pattern discovery, segmentation, and feature learning*.

    ---

    ### Why Do We Use It?
    - Customer segmentation in marketing  
    - Image compression  
    - Anomaly detection  
    - Preprocessing for supervised models  

    ---

    ### How It Works
    1. *Initialize* random centroids  
    2. *Assign* each data point to the nearest centroid using *Euclidean distance*  
    3. *Update* centroids by averaging points in each cluster  
    4. Repeat until:
       - No cluster changes, OR
       - Centroids stabilize, OR
       - Maximum iterations reached

    ---

    ### Distance Formula
    d(p,c) = √((p₁-c₁)² + (p₂-c₂)² + ... + (pₙ-cₙ)²)

    ---

    ### Stopping Criteria
    - No change in cluster assignments  
    - Centroids stabilize  
    - Maximum iterations reached  

    ---

    ### Complexity
    O(n × k × i)
    - *n* → data points  
    - *k* → clusters  
    - *i* → iterations  
    """)

uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file:
    X = load_data(uploaded_file)

    if X.shape[1] < 3:
        st.warning("⚠ Please upload a dataset with at least 3 numeric columns.")
    else:
        st.success("✅ Data loaded and preprocessed successfully!")

        st.subheader("Data Preview")
        st.dataframe(X.head())

        k = st.slider("Select number of clusters (k)", min_value=2, max_value=10, value=3)
        clusters = run_kmeans(X, k)

        st.subheader("3D Cluster Visualization")
        fig = plot_clusters(X, clusters)
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Cluster Counts")
        cluster_counts = pd.Series(clusters).value_counts().reset_index()
        cluster_counts.columns = ["Cluster", "Count"]
        st.table(cluster_counts)
else:
    st.info("⬆ Please upload a CSV file to get started.")

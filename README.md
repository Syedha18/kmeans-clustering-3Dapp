# K-Means 3D Clustering

K-Means 3D Clustering is an interactive web application built using *Streamlit*.  
It applies the *K-Means clustering algorithm* to datasets (like the Iris dataset) and visualizes the results in an interactive 3D graph.  
This project demonstrates unsupervised machine learning in an intuitive and visual way.

---

## Why This Project
Clustering is a powerful unsupervised learning technique used to group similar data points.  
The Iris dataset is a classic example for clustering, and this project enhances understanding by:
- Allowing interactive selection of the number of clusters (k)
- Visualizing results in 3D for better intuition
- Showing the distribution of data points across clusters

This project is ideal for:
- Machine Learning beginners to learn clustering
- Data visualization enthusiasts
- Deploying and sharing ML apps online

---

## Features
- Load datasets (example: Iris dataset)
- Select the number of clusters (k)
- Apply K-Means clustering with Scikit-learn
- View 3D visualization of the clusters using Plotly
- Display the count of data points in each cluster
- Deployable to Streamlit Cloud with one click

---

## Tech Stack
- *Python* – Core programming language
- *Streamlit* – For building the interactive web application
- *Pandas* – Data loading and manipulation
- *Scikit-learn* – K-Means clustering algorithm
- *Plotly* – 3D visualization
- *GitHub* – Version control and hosting the project repository

---

## Project Structure

kmeans-clustering-3Dapp/ │ ├── data_loader.py        # Handles loading and preprocessing datasets ├── kmeans_model.py       # Implements K-Means clustering logic ├── visualize.py          # 3D plotting using Plotly ├── streamlit_app.py      # Main Streamlit application ├── requirements.txt      # Project dependencies └── README.md             # Documentation

---

## How K-Means Works
1. *Initialization:* Choose k initial random centroids.
2. *Assignment:* Assign each data point to the nearest centroid.
3. *Update:* Calculate the mean of all points assigned to each centroid to update its position.
4. *Repeat:* Continue assignment and update steps until the centroids stop moving (convergence).

---

## How the 3D Visualization Works
- After clustering is completed, each data point is assigned a cluster label.
- We use *Plotly* to create an interactive 3D scatter plot with:
  - *X-axis:* Feature 1 (e.g., Sepal length)
  - *Y-axis:* Feature 2 (e.g., Sepal width)
  - *Z-axis:* Feature 3 (e.g., Petal length)
  - *Color:* Cluster assignment (each cluster has a unique color)

- Example output for k=3:
  - Cluster 0 → 42 points
  - Cluster 1 → 50 points
  - Cluster 2 → 58 points

This helps visualize how the algorithm grouped data points into clusters and how well the boundaries are separated in feature space.

---

## Example Dataset
This project uses the *Iris dataset* as a default example:

| Species       | Count |
|---------------|--------|
| Setosa        | 50     |
| Versicolor    | 50     |
| Virginica     | 50     |

Each data point has 4 features:
- Sepal length
- Sepal width
- Petal length
- Petal width

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/Syedha18/kmeans-clustering-3Dapp.git
cd kmeans-clustering-3Dapp

2. Install dependencies

pip install -r requirements.txt

3. Run the Streamlit app

streamlit run streamlit_app.py


---

Deployment

This project can be deployed easily on Streamlit Cloud:

1. Push your code to GitHub.


2. Go to Streamlit Cloud.


3. Connect your GitHub repository.


4. Select the main file path (streamlit_app.py).


5. Click Deploy.



Your app will be live and shareable with others.


---

Requirements

Create a requirements.txt file containing:

streamlit
pandas
scikit-learn
plotly


---

Future Enhancements

Add support for uploading custom datasets.

Allow dynamic selection of clustering features.

Improve visualization with silhouette scores.

Add other clustering algorithms (DBSCAN, Hierarchical).



---

License

This project is open-source and available under the MIT License.


---


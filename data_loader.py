import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(file):
    # Load CSV file
    data = pd.read_csv(file)

    # ⿡ Handle missing values - remove rows with nulls
    data = data.dropna()

    # ⿢ Remove duplicate rows
    data = data.drop_duplicates()

    # ⿣ Select only numeric columns
    numeric_data = data.select_dtypes(include=[np.number])

    # ⿤ Take only first 3 columns (for 3D clustering)
    numeric_data = numeric_data.iloc[:, :3]

    # ⿥ Scale the data (important for K-Means)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_data)

    return scaled_data

import pandas as pd
import numpy as np

def load_data(file):
    # Read CSV
    data = pd.read_csv(file)

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Handle missing values (remove rows with null values)
    data = data.dropna()

    # Select only numeric columns
    numeric_data = data.select_dtypes(include=[np.number])

    # Take first 3 numeric columns if more exist
    numeric_data = numeric_data.iloc[:, :3]

    return numeric_data  # Always return DataFrame
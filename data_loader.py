import pandas as pd
import numpy as np

def load_data(file):
    data = pd.read_csv(file)
    # Only numeric columns
    numeric_data = data.select_dtypes(include=[np.number])
    # Take first 3 columns if more exist
    return numeric_data.iloc[:,:3]
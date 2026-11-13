import pandas as pd

def load_data():
    data = pd.read_excel("../data/raw/dataset-uci.xlsx")
    y = data["Case Type"].astype("int64")
    X = data.drop(columns=["Case Type", "Unnamed: 0"], errors="ignore")
    return X, y
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold

from src.config import cols_age

df = pd.read_excel("../data/raw/dataset-uci.xlsx")

cols_bin = [
    col for col in df.columns
    if col not in cols_age + ["Case Type", "Unnamed: 0"]
]

# Case Type est déjà codée 0/1; on garde ces valeurs sans supposer leur signification.
y = df["Case Type"].astype("int64")
X = df.drop(columns=["Case Type", "Unnamed: 0"])


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)

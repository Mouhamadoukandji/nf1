from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

from src.config import cols_age
from src.data import cols_bin

# Définition du pipeline de prétraitement
prepro = ColumnTransformer([
    ("ages", Pipeline([
        ("imp", SimpleImputer(strategy="median")),
        ("sc", StandardScaler()),
    ]), cols_age),
    ("bin", "passthrough", cols_bin),
])

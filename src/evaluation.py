from sklearn.model_selection import cross_validate, GridSearchCV, StratifiedKFold
from sklearn.metrics import f1_score, confusion_matrix

metriques = ["f1_macro", "recall", "precision", "accuracy", "roc_auc"]
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

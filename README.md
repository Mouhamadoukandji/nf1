## Architecture à suivre

projet-nf1/
├── README.md               ← installer, lancer, résumé des résultats
├── requirements.txt        ← versions exactes (scikit-learn==1.9.1, pandas…)
├── .gitignore              ← data/raw/, .ipynb_checkpoints, __pycache__
│
├── data/
│   ├── raw/                ← fichier UCI original, jamais modifié
│   └── processed/          ← 296 patients filtrés, générés par le code
│
├── src/                    ← code commun, écrit ensemble au début
│   ├── config.py           ← chemins, RANDOM_STATE, noms des colonnes, cible
│   ├── data.py             ← chargement + filtrage des témoins + X, y
│   ├── preprocessing.py    ← pipeline : imputation (âges) + normalisation
│   └── evaluation.py       ← validation croisée imbriquée stratifiée + métriques
│
├── notebooks/
│   ├── 01_exploration_idrissa.ipynb      ← distribution de la cible, manquants, χ²
│   ├── 02_logreg_idrissa.ipynb           ← grille C, l1_ratio + interprétation des poids
│   ├── 03_svm_falilou.ipynb              ← linéaire vs RBF, grille C, gamma
│   ├── 04_random_forest_falilou.ipynb    ← grille profondeur, feuilles + importance par permutation
│   └── 05_comparaison_finale.ipynb       ← ensemble : baseline, tableau, boxplots, modèle final
│
├── results/
│   ├── baseline.csv
│   ├── logreg.csv
│   ├── svm.csv
│   ├── random_forest.csv   ← scores des 5 tours externes, par métrique
│   └── figures/
│
└── rapport/
    ├── validation.pdf      ← le protocole demandé par l'enseignant
    └── rapport_final/
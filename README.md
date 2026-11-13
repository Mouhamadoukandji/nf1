# Classification des cas de neurofibromatose de type 1 (NF1)

**Question :** les symptômes d'un patient permettent-ils de savoir si sa NF1 est **familiale** (héritée d'un parent) ou **sporadique** (mutation nouvelle) ?

**Réponse courte :** non. Aucun des trois modèles testés ne fait mieux que le hasard.

Projet de fouille de données — Master 2 SID, Aix-Marseille Université.
Auteurs : **SECK Idrissa** et **KANDJI Mouhamadou Falilou**.

---

## Les données

- Source : [UCI — Neurofibromatosis Type 1; Clinical Symptoms of Familial and Sporadic Cases](https://archive.ics.uci.edu/dataset/1162/neurofibromatosis+type+1+clinical+symptoms+of+familial+and+sporadic+cases)
- 296 patients : 161 sporadiques (0) et 135 familiaux (1)
- 18 variables : 3 âges (mère, père, premier diagnostic) et 15 variables binaires (symptômes)

Le fichier de données n'est pas dans le dépôt. Téléchargez-le depuis UCI et placez-le ici :

```
data/raw/dataset-uci.xlsx
```

---

## Organisation du dépôt

```
projet-nf1/
├── src/                     code commun, utilisé par les carnets 02 à 05
│   ├── config.py            noms des colonnes d'âge
│   ├── data.py              chargement, X / y, découpage train / test (80 / 20)
│   ├── preprocessing.py     imputation des âges (médiane) + standardisation
│   └── evaluation.py        métriques et découpage de la validation croisée
├── notebooks/
│   ├── exploration.ipynb      analyse des données
│   ├── logreg.ipynb           régression logistique
│   ├── svm.ipynb              SVM
│   ├── random_forest.ipynb    forêt aléatoire
│   └── comparaison_finale.ipynb       baselines + comparaison
├── results/                 scores de chaque modèle (fichiers .csv) et figures
└── rapport/                 rapport final
```

---

## Installation

Python 3.13.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows : .venv\Scripts\activate
pip install -r requirements.txt
```

---

## Lancer le projet

Ouvrez les notebook **depuis le dossier `notebooks/`** et exécutez-les **dans l'ordre** :

1. chaque notebook de modèle enregistre ses scores dans `results/`.
2. `comparaison_finale : il relit ces scores et compare les modèles.

---

## Méthode, en bref

- **Découpage stratifié** : 80 % entraînement, 20 % test, même proportion de familiaux partout.
- **Pas de fuite de données** : l'imputation et la standardisation sont dans un `Pipeline`, donc apprises uniquement sur les données d'entraînement.
- **Validation croisée imbriquée stratifiée (5 × 5)** : la boucle interne choisit les hyperparamètres, la boucle externe mesure la performance sur des patients jamais vus.
- **Métrique principale** : F1 macro (les deux classes comptent autant). On rapporte aussi l'AUC.

---

## Résultats

Validation croisée imbriquée sur les 236 patients d'entraînement (moyenne ± écart-type sur 5 plis).

| Modèle | F1 macro | AUC |
|---|---|---|
| Baseline « toujours sporadique » | 0,35 | 0,50 |
| Baseline « hasard » | ≈ 0,50 | ≈ 0,50 |
| Régression logistique | 0,47 ± 0,03 | 0,45 |
| SVM | 0,45 ± 0,04 | 0,46 |
| Forêt aléatoire | 0,41 ± 0,02 | 0,44 |

**Lecture :** les trois modèles sont au niveau du hasard (AUC autour de 0,5). Les hyperparamètres choisis changent d'un pli à l'autre, signe qu'aucun réglage n'est meilleur qu'un autre.

---

## Conclusion

Dans ces données, les symptômes ne distinguent pas les cas familiaux des cas sporadiques. C'est cohérent avec la biologie : dans les deux cas, c'est le même gène qui est touché. Le caractère familial se détermine par l'histoire familiale et le test génétique, pas par les symptômes.

**Limites :** 296 patients seulement, âge du patient au moment de l'examen absent, définition du caractère « familial » non documentée dans la source.

Référence : Sharafi et al., *A machine learning approach for predicting familial and sporadic disease cases based on clinical symptoms*, Türk Hijyen ve Deneysel Biyoloji Dergisi, 2025.
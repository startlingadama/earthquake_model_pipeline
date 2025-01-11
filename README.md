# Projet de Prédiction de la Magnitude d'un Tremblement de Terre

Ce projet vise à prédire la magnitude d'un tremblement de terre en utilisant un modèle de **stacking** avec **scikit-learn** et **XGBoost**. Le pipeline est géré avec **DVC** pour assurer la reproductibilité et la versioning des données, des modèles, et des métriques.

---

## Objectif du Projet

L'objectif est de développer un modèle de machine learning capable de prédire la magnitude d'un tremblement de terre en fonction de caractéristiques telles que la localisation, la profondeur, et d'autres paramètres sismiques. Le modèle utilise une approche de **stacking** pour combiner les prédictions de plusieurs modèles de base (comme **DecisionTreeRegressor** et **XGBRegressor**) afin d'améliorer la précision.

---

## Structure du Projet

````
mon_projet/
├── data/
│   ├── raw/                  # Données brutes
│   ├── processed/            # Données prétraitées
│       └── data.csv          # Données utilisées pour l'entraînement et l'évaluation
├── scripts/
│   ├── train.py              # Script pour entraîner le modèle
│   ├── evaluate.py           # Script pour évaluer le modèle
│   ├── deploy.py             # Script pour déployer le modèle
├── models/
│   └── stacking_model.pkl    # Modèle entraîné sauvegardé
├── metrics/
│   └── metrics.txt           # Métriques d'évaluation du modèle
├── dvc.yaml                  # Fichier de configuration du pipeline DVC
├── params.yaml               # Fichier de paramètres pour le modèle
└── README.md                 # Documentation du projet
````
---

## Étapes du Pipeline

Le pipeline est composé des étapes suivantes :

1. **Prétraitement des données** :
   - Les données brutes sont nettoyées et préparées pour l'entraînement.
   - Les données prétraitées sont sauvegardées dans `data/processed/data.csv`.

2. **Entraînement du modèle** :
   - Le modèle de stacking est entraîné en utilisant les données prétraitées.
   - Le modèle entraîné est sauvegardé dans `models/stacking_model.pkl`.

3. **Évaluation du modèle** :
   - Le modèle est évalué sur un ensemble de test.
   - Les métriques (MSE, RMSE, MAE, R²) sont calculées et sauvegardées dans `metrics/metrics.txt`.

4. **Déploiement du modèle** :
   - Le modèle est déployé dans un dossier `deploy/` pour une utilisation future.

---

## Métriques d'Évaluation

Les métriques suivantes sont utilisées pour évaluer les performances du modèle :

- **MSE (Mean Squared Error)** : Mesure la moyenne des carrés des erreurs.
- **RMSE (Root Mean Squared Error)** : Racine carrée du MSE.
- **MAE (Mean Absolute Error)** : Mesure la moyenne des valeurs absolues des erreurs.
- **R² (Coefficient of Determination)** : Mesure la proportion de la variance expliquée par le modèle.

---

## Comment Exécuter le Projet

### Prérequis

- **Python 3.8+**
- **DVC**
- **scikit-learn**
- **XGBoost**
- **pandas**
- **numpy**

Installez les dépendances avec :

```bash
pip install dvc scikit-learn xgboost pandas numpy
```

### Étapes pour Exécuter le Pipeline

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/startlingadama/earthquake_model_pipeline.git
   cd mon_projet
   ```

2. **Initialiser DVC** :
   ```bash
   dvc init
   ```

3. **Ajouter les données à suivre** :
   ```bash
   dvc add data/processed/data.csv
   ```

4. **Exécuter le pipeline** :
   ```bash
   dvc repro
   ```

   Cela exécutera les étapes suivantes :
   - Entraînement du modèle (`train.py`).
   - Évaluation du modèle (`evaluate.py`).
   - Déploiement du modèle (`deploy.py`).

5. **Vérifier les métriques** :
   Les métriques d'évaluation sont sauvegardées dans `metrics/metrics.txt`. Vous pouvez les consulter avec :
   ```bash
   cat metrics/metrics.txt
   ```

---

## Fichiers de Configuration

### `params.yaml`

Ce fichier contient les paramètres pour l'entraînement du modèle. Les paramètres incluent la taille de l'ensemble de test, les hyperparamètres de XGBoost, etc.

### `dvc.yaml`

Ce fichier définit les étapes du pipeline DVC, y compris les dépendances et les sorties de chaque étape.

---

## Scripts

- **`train.py`** : Entraîne un modèle de stacking avec **DecisionTreeRegressor** et **XGBRegressor**.
- **`evaluate.py`** : Évalue le modèle en calculant les métriques (MSE, RMSE, MAE, R²).
- **`deploy.py`** : Déploie le modèle en le copiant dans un dossier `deploy/`.

---

## Résultats

Les métriques d'évaluation sont sauvegardées dans `metrics/metrics.txt`. Voici un exemple de sortie :

```
example
MSE: 10.25
RMSE: 3.20
MAE: 2.50
R²: 0.92
```

---

## Améliorations Futures

- **Optimisation des hyperparamètres** : Utiliser des techniques comme la recherche par grille ou la recherche aléatoire pour optimiser les hyperparamètres.
- **Validation croisée** : Ajouter une validation croisée pour évaluer la robustesse du modèle.
- **Déploiement cloud** : Déployer le modèle sur un service cloud comme AWS SageMaker ou Google AI Platform.

---

## Auteurs

- Votre Nom (votre.email@example.com)

---

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---

### **Pourquoi cette version est-elle préférable ?**

1. **Clarté et concision** :
   - Le `README.md` est plus facile à lire et à comprendre sans être encombré de code.

2. **Référence aux fichiers** :
   - Les scripts (`train.py`, `evaluate.py`, `deploy.py`) et les fichiers de configuration (`params.yaml`, `dvc.yaml`) sont mentionnés, mais leur contenu n'est pas dupliqué dans le `README.md`.

3. **Maintenabilité** :
   - Si le code change, vous n'avez pas besoin de mettre à jour le `README.md` (sauf si les instructions ou la structure du projet changent).

4. **Orientation utilisateur** :
   - Le `README.md` se concentre sur ce dont un utilisateur a besoin pour comprendre et exécuter le projet, sans entrer dans les détails techniques du code.

---

### **Quand inclure du code dans le README.md ?**

Il peut être utile d'inclure de petits extraits de code dans le `README.md` pour :
- Montrer un exemple d'utilisation rapide.
- Expliquer une configuration spécifique.
- Donner des commandes CLI ou des snippets de code courts.

Cependant, pour des scripts complets ou des fichiers de configuration, il est préférable de les laisser dans leurs fichiers respectifs et de simplement y faire référence dans le `README.md`.

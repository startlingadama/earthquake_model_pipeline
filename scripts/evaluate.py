import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import yaml

# Charger les paramètres
with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)

# Charger les données de test
data = pd.read_csv("data/processed/data.csv")
X_test = data.drop("target", axis=1)
y_test = data["target"]

# Charger le modèle
model = joblib.load("models/stacking_model.pkl")

# Faire des prédictions
y_pred = model.predict(X_test)

# Calculer les métriques
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)  # Racine carrée du MSE
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Afficher les résultats
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"MAE: {mae}")
print(f"R²: {r2}")

# Sauvegarder les métriques dans un fichier
with open("metrics/metrics.txt", "w") as f:
    f.write(f"MSE: {mse}\n")
    f.write(f"RMSE: {rmse}\n")
    f.write(f"MAE: {mae}\n")
    f.write(f"R²: {r2}\n")
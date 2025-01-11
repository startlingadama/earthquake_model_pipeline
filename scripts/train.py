import pandas as pd
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import yaml

# Charger les paramètres
with open("params.yaml", "r") as f:
    params = yaml.safe_load(f)

# Charger les données
data = pd.read_csv("data/processed/data.csv")
X = data.drop("target", axis=1)
y = data["target"]

# Diviser les données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=params["train"]["test_size"], random_state=42)

# Définir les modèles de base
base_models = [
    ('dt', DecisionTreeRegressor(random_state=42)),
    ('xgb', XGBRegressor(**params["xgb"]))  # Ajouter XGBoost comme modèle de base
]

# Définir le modèle de stacking
stacking_model = StackingRegressor(
    estimators=base_models,
    final_estimator=LinearRegression(),  # Utiliser LinearRegression comme métamodèle
    cv=params["train"]["cv"]
)

# Entraîner le modèle
stacking_model.fit(X_train, y_train)

# Sauvegarder le modèle
joblib.dump(stacking_model, "models/stacking_model.pkl")

# Évaluer le modèle
y_pred = stacking_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"MSE: {mse}")
print(f"R²: {r2}")
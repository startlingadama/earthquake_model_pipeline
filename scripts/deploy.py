# scripts/deploy.py
import joblib
import shutil

# Copier le modèle vers un dossier de déploiement
shutil.copy("models/stacking_model.pkl", "deploy/stacking_model.pkl")
print("Modèle déployé avec succès.")

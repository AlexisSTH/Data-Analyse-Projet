import pandas as pd
import joblib

# Chargement des données de test
X_test = pd.read_csv("X_test.csv")

# Chargement du modèle
model = joblib.load("modele_ventes.pkl")

# Prédictions
y_pred = model.predict(X_test)

# Sauvegarde des prédictions
df_pred = pd.DataFrame({"y_pred": y_pred})
df_pred.to_csv("y_pred.csv", index=False)

print("Prédictions terminées. Fichier créé : y_pred.csv")

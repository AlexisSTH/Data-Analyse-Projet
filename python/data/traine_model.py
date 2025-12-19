import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib 

# Chargement des données d'entraînement
X_train = pd.read_csv("X_train.csv")
y_train = pd.read_csv("y_train.csv")

# y_train doit être un vecteur 1D
y_train = y_train.values.ravel()

# Définition et entraînement du modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Sauvegarde du modèle entraîné
joblib.dump(model, "modele_ventes.pkl")

print("Modèle entraîné et sauvegardé dans 'modele_ventes.pkl'")

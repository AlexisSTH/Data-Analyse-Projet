import pandas as pd
from sklearn.model_selection import train_test_split

# Chargement du CSV
df = pd.read_csv("data_nettoyee.csv")

# Suppression des ligne avec prix = 0
df = df[df["prix"] > 0]

# Conversion de la date
df["date_vente"] = pd.to_datetime(df["date_vente"])

# Création d'une colonne "mois"
df["mois"] = df["date_vente"].dt.month

# Encodage des variables catégorielles (pays, canal)
df_model = pd.get_dummies(
    df,
    columns=["pays", "canal"],
    drop_first=True
)

# Variable cible
y = df_model["quantite"]

# Variables explicatives : on enlève ce qui ne sert pas au modèle
x = df_model.drop(columns=["quantite", "produit", "date_vente", "id"])

# Split train / test
x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

# Sauvegarde des jeux de données
x_train.to_csv("X_train.csv", index=False)
x_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("Chargement et préparation terminés. Fichiers créés : X_train.csv, X_test.csv, y_train.csv, y_test.csv")

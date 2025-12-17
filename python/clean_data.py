import pymysql # pyright: ignore[reportMissingModuleSource]
import pandas as pd

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="chanel"
)

query = "SELECT * FROM vente_chanel;"
df = pd.read_sql(query, conn)

print("Données brutes chargées : ")
print(df.head())
print(df.info())

#  NETTOYAGE DES DONNÉES

# Supprimer les doublons
df = df.drop_duplicates()

# PAYS
df['pays'] = df['pays'].str.strip().str.lower()

corrections_pays = {
    'frnace': 'france',
    'u.s.a': 'usa',
    'us': 'usa',
    'united states': 'usa',
    'uk': 'royaume-uni'
}

df['pays'] = df['pays'].replace(corrections_pays)
df['pays'] = df['pays'].str.upper()

# CANAL (accepter que Boutique ou Online)
df['canal'] = df['canal'].str.strip().str.lower()

corrections_canal = {
    'store': 'Boutique',
    'boutique': 'Boutique',
    'web': 'Online',
    'online': 'Online'
}

df['canal'] = df['canal'].replace(corrections_canal)
df['canal'] = df['canal'].str.title()

# Gestion des prix NULL 
prix_median = df['prix'].median()
df['prix'] = df['prix'].fillna(prix_median)

# Suppression des ventes avec quantité = 0
filtre_quantite = df['quantite'] > 0
df = df[filtre_quantite]

# Après nettoyage faut le print
print("\n Données après nettoyage: ")
print(df.head())
print(df.info())
df.to_csv("data_nettoyee.csv", index=False)
conn.close()

print("\n Nettoyage terminé")

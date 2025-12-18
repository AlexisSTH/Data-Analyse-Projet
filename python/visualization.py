import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Charger les données nettoyées
df = pd.read_csv("data/data_nettoyee.csv")

# Convertir la date
df['date_vente'] = pd.to_datetime(df['date_vente'])

# Créer le chiffre d'affaires
df['chiffre_affaires'] = df['quantite'] * df['prix']

# PAYS
ca_pays = df.groupby('pays')['chiffre_affaires'].sum()

plt.figure()
ca_pays.plot(kind='bar')
plt.title("Chiffre d'affaires par pays")
plt.xlabel("Pays")
plt.ylabel("Chiffre d'affaires (€)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Canal
ventes_canal = df.groupby('canal')['quantite'].sum()

plt.figure()
ventes_canal.plot(kind='bar')
plt.title("Quantité vendue par canal")
plt.xlabel("Canal")
plt.ylabel("Quantité vendue")
plt.tight_layout()
plt.show()


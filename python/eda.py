import pandas as pd

df = pd.read_csv("data_nettoyee.csv")

print(df.head())
print(df.info())

print("\nQuantité totale vendue : ", df['quantite'].sum())

df['chiffre_affaires'] = df['quantite'] * df['prix']
print("Chiffre d’affaires total :", df['chiffre_affaires'].sum())

print("\nVentes par pays :")
print(df.groupby('pays')['quantite'].sum())

print("\nVentes par canal :")
print(df.groupby('canal')['quantite'].sum())
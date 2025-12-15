import pymysql # pyright: ignore[reportMissingModuleSource]
import pandas as pd

# Connexion à MySQL (XAMPP) avec PyMySQL
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="chanel"
)

query = "SELECT * FROM vente_chanel;"

df = pd.read_sql(query, conn)

print("Aperçu des données :")
print(df.head())

print("\nInformations sur les données :")
print(df.info())

print("\nVoici toutes les données :")
print(df)

conn.close()

import pandas as pd
import matplotlib.pyplot as plt

# 1) Charger les valeurs réelles et prédites depuis les CSV
y_test = pd.read_csv("y_test.csv").values.ravel()         
y_pred = pd.read_csv("y_pred.csv")["y_pred"].values        

# 2) Mettre dans un DataFrame pour analyser les erreurs
df_errors = pd.DataFrame({
    "y_reel": y_test,
    "y_pred": y_pred
})

df_errors["erreur"] = df_errors["y_reel"] - df_errors["y_pred"]
df_errors["erreur_absolue"] = df_errors["erreur"].abs()
df_errors["erreur_pourcent"] = df_errors["erreur_absolue"] / df_errors["y_reel"] * 100

# 3) Graphique 1 : réel vs prédit
plt.figure(figsize=(8, 5))
plt.scatter(df_errors["y_reel"], df_errors["y_pred"], alpha=0.7)
plt.plot(
    [df_errors["y_reel"].min(), df_errors["y_reel"].max()],
    [df_errors["y_reel"].min(), df_errors["y_reel"].max()],
    color="red", linestyle="--", label="y = x (prédiction parfaite)"
)
plt.xlabel("Ventes réelles")
plt.ylabel("Ventes prédites")
plt.title("Bleu de Chanel – Ventes réelles vs prédites")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

import pandas as pd
import numpy as np
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error
)

# Chargement des vraies valeurs et des prédictions
y_test = pd.read_csv("y_test.csv")
y_pred = pd.read_csv("y_pred.csv")

# Conversion en vecteurs 1D
y_test = y_test.values.ravel()
y_pred = y_pred["y_pred"].values

# Calcul des métriques
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mape = mean_absolute_percentage_error(y_test, y_pred) * 100  # en %

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"MAPE : {mape:.2f}%")

if mape < 70:
    print("Objectif atteint : MAPE < 70%")
else:
    print("Objectif NON atteint : MAPE >= 70% ")

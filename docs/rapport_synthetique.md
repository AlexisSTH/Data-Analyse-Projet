# Rapport Synthétique – Projet d’analyse et prédiction des ventes

## 1. Contexte et objectif

Dans le cadre de ce projet, l’objectif est de partir de données de ventes brutes stockées dans une base **MySQL** pour :

- analyser les ventes (par pays, par canal, par prix, par quantité et par date de vente.) ;
- entraîner un modèle de **machine learning** pour prédire les ventes ;
- évaluer la qualité de ces prédictions avec des indicateurs d’erreur.

L’idée est de construire une **petite chaîne de traitement de données de bout en bout**, depuis la base SQL jusqu’à l’évaluation du modèle.

---

## 2. Technologies utilisées

- **Base de données** : MySQL  
- **Langage** : Python  
- **Librairies principales** :  
  - `pymysql` pour la connexion à MySQL  
  - `pandas` pour la manipulation de données  
  - `scikit-learn` `LinearRegression` pour le modèle de machine learning  
  - `matplotlib` / `seaborn` pour les visualisations

---

## 3. Étapes principales du projet

1. **Création et alimentation de la base MySQL**
   - Création de la table de ventes (`vente_chanel`).
   - Insertion des données brutes de ventes.
   - Suppression des anciens fichiers CSV inutiles : la base MySQL devient la source principale.

2. **Chargement et nettoyage des données dans Python**
   - Connexion à MySQL avec `pymysql`.
   - Chargement des données dans un DataFrame `pandas`.
   - Nettoyage : harmonisation des pays (mise en majuscules), corrections et préparation d’un fichier `data_nettoyee`.

3. **Analyse exploratoire (EDA)**
   - Calculs et visualisations pour comprendre les ventes, par exemple :
     - **chiffre d’affaires total par pays** ;
     - **quantité vendue par canal**.
   - Ces graphiques permettent d’identifier les pays et canaux les plus importants.

4. **Modélisation et prédiction**
   - Séparation des données en **jeu d’entraînement** et **jeu de test**.
   - Entraînement d’un **modèle de régression** pour prédire une variable liée aux ventes.
   - Sauvegarde du modèle entraîné dans un fichier `.pkl`.
   - Création d’un script de **prédiction** pour générer des valeurs prédites à partir de nouvelles données.

5. **Évaluation du modèle**
   - Calcul de plusieurs métriques d’erreur :
     - **MAE (Mean Absolute Error)** : 1,26  
     - **RMSE (Root Mean Squared Error)** : 1,48  
     - **MAPE (Mean Absolute Percentage Error)** : **66,74 %**
   - Visualisation des erreurs à l’aide d’un **graphique d’analyse des erreurs**.

---

## 4. Résultats et interprétation

Les métriques obtenues sont les suivantes :

- **MAE = 1,26** : en moyenne, l’écart absolu entre la valeur réelle et la valeur prédite est de 1,26 unité.  
- **RMSE = 1,48** : les erreurs plus importantes sont davantage pénalisées ; cette valeur reste relativement proche du MAE.  
- **MAPE = 66,74 %** : en moyenne, le modèle se trompe d’environ **67 %** par rapport aux valeurs réelles.

Cela signifie que, si la vraie valeur est 100, la prédiction typique du modèle peut se situer autour de 33 ou 167 (100 − 67 / 100 + 67).  
Le **MAPE est donc assez élevé**, ce qui indique que le modèle reste **peu précis**

Le **graphique d’analyse des erreurs** permet de voir :

- si le modèle a tendance à **sous-estimer** ou **surestimer** les ventes ;
- si certaines observations ont une erreur beaucoup plus forte que les autres ;
- si l’erreur varie selon certains profils (pays, canaux, etc.).

---

## 5. Pistes d’amélioration

Plusieurs améliorations sont possibles :

- Tester d’autres **modèles de machine learning** (modèles non linéaires, arbres, forêts aléatoires) ;
- Ajouter plus de **variables explicatives** (saisonnalité, type de produit, promotions, autres.) ;
- Mettre en place une **validation croisée** pour mieux évaluer la robustesse du modèle ;
- Affiner le nettoyage et le prétraitement (normalisation, encodage plus fin, gestion des outliers) ;
- Automatiser la mise à jour des données depuis la base MySQL.

---

## 6. Rapport détaillé

Pour une description plus complète des étapes, du code et des graphiques, se référer au :

👉 Rapport détaillé : `docs/rapport_detaille.md`

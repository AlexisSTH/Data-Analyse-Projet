# Rapport détaillé – Projet d’analyse de données et prédiction des ventes

## 1. Contexte et objectifs

Ce projet a pour objectif de construire une **chaîne complète d’analyse de données** à partir de ventes enregistrées dans une base **MySQL**, puis de développer un **modèle de prédiction** des ventes en Python.

Les objectifs principaux sont :

- centraliser les données de ventes dans une **base relationnelle** structurée ;
- réaliser une **analyse exploratoire** pour mieux comprendre les ventes (par pays, par canal, etc.) ;
- entraîner un **modèle de machine learning** afin de prédire des valeurs liées aux ventes ;
- évaluer la qualité des prédictions à l’aide de plusieurs **indicateurs d’erreur** (MAE, RMSE, MAPE) et d’un **graphique d’analyse des erreurs**.

Ce projet s’inscrit dans une démarche de **data pipeline** de bout en bout, depuis la source de données jusqu’à l’évaluation d’un modèle.

---

## 2. Données et base MySQL

### 2.1. Source des données

Les données utilisées correspondent à des **transactions de ventes** comprenant, par exemple :

- un identifiant de transaction ;
- des informations sur le produit ;
- la **quantité** vendue ;
- le **prix** ;
- le **pays** ;
- le **canal de vente**.

Ces données ont été importées dans une base **MySQL** pour permettre :

- une meilleure **structuration** ;
- l’écriture de **requêtes SQL** d’analyse ;
- et une intégration propre avec Python.

### 2.2. Modélisation dans MySQL

Une table principale de ventes, nommée par exemple `vente_chanel`, a été créée.  
Elle contient notamment les champs nécessaires à l’analyse, comme :

- un identifiant de ligne de vente ;
- la date de la transaction ;
- le pays ;
- le canal de vente ;
- la quantité ;
- le prix unitaire ou le montant total.

Un script SQL de **création de table** a été ajouté au projet, ainsi que des scripts ou fichiers d’**insertion de données** pour alimenter la table avec les ventes historiques.

Les anciens fichiers **CSV bruts** qui n’étaient plus utilisés ont été supprimés du projet, la **base MySQL** devenant la nouvelle source de référence.

---

## 3. Architecture technique

L’architecture du projet repose sur les éléments suivants :

- **MySQL** : stockage structuré des données de ventes ;
- **Python** : langage principal pour l’analyse de données et la modélisation ;
- **`pymysql`** : pour se connecter à MySQL et exécuter des requêtes ;
- **`pandas`** : pour manipuler les données sous forme de DataFrames ;
- **Bibliothèque de machine learning** (par ex. `scikit-learn`) : pour l’entraînement du modèle de prédiction ;
- **`matplotlib` / `seaborn`** : pour la création de graphiques (EDA, courbes d’erreurs, etc.).

L’ensemble du code Python est organisé en plusieurs scripts (chargement des données, nettoyage, EDA, modélisation, prédiction, calcul d’erreur, etc.), ce qui facilite la compréhension du pipeline.

---

## 4. Chargement et nettoyage des données

### 4.1. Connexion à la base MySQL

Une connexion à la base MySQL est réalisée via `pymysql`.  
Les principales étapes sont :

1. se connecter à la base (hôte, utilisateur, mot de passe, nom de la base) ;
2. exécuter une requête SQL de type `SELECT` sur la table `vente_chanel` ;
3. récupérer le résultat dans un DataFrame `pandas`.

Un premier affichage de **quelques lignes** permet de vérifier que les données ont été correctement importées.

### 4.2. Étapes de nettoyage

Les principales transformations réalisées lors du nettoyage sont notamment :

- **Harmonisation des pays** : les noms de pays ont été transformés en **majuscules** pour éviter les doublons du type `France` / `FRANCE` / `france` ;
- Création d’un jeu de données nettoyé, enregistré dans un fichier (par exemple `data_nettoyee`), afin de séparer clairement les données brutes des données prêtes à l’analyse ;
- Vérifications visuelles (statistiques descriptives, recherche de valeurs manquantes, cohérence des types, etc.).

L’objectif de cette étape est de disposer d’un jeu de données **cohérent et propre**, prêt à être utilisé pour l’analyse exploratoire puis la modélisation.

---

## 5. Analyse exploratoire des données (EDA)

Une **analyse exploratoire des données (Exploratory Data Analysis)** a été réalisée afin de mieux comprendre le comportement des ventes.

### 5.1. Indicateurs et visualisations

Parmi les analyses mises en place :

- **Chiffre d’affaires total par pays**  
  Un graphique représente le montant total des ventes pour chaque pays, ce qui permet d’identifier les marchés les plus importants.

- **Quantité vendue par canal de vente**  
  Un autre graphique montre la quantité totale vendue en fonction du canal (par exemple : online, retail, grossiste, etc., selon la structure des données).

Ces graphiques aident à :

- repérer les pays ou canaux dominants ;
- détecter des déséquilibres ;
- préparer la réflexion sur les variables qui pourraient influencer les ventes dans le modèle de prédiction.

---

## 6. Préparation des données pour le modèle

Avant l’entraînement du modèle, les données sont préparées de la façon suivante :

1. **Sélection de la variable cible et des variables explicatives**  
   - Choix de la variable à prédire (par exemple, montant de vente ou quantité) ;
   - Sélection des variables explicatives pertinentes (pays, canal, variables numériques, etc.).

2. **Encodage des variables catégorielles**  
   - Transformation des variables textuelles (comme le pays, le canal) en variables numériques, si nécessaire (par exemple avec un encodage one-hot).

3. **Division en jeu d’entraînement et jeu de test**  
   - Séparation des données en deux sous-ensembles :
     - un **jeu d’entraînement** pour apprendre le modèle ;
     - un **jeu de test** pour évaluer ses performances sur des données jamais vues.

Cette préparation est indispensable pour garantir une évaluation correcte du modèle.

---

## 7. Modélisation et prédiction

Un **modèle de régression supervisée** a été mis en place pour prédire une variable liée aux ventes.

### 7.1. Entraînement du modèle

Les principales étapes sont :

- instanciation du modèle (par exemple un modèle de **régression linéaire** ou un autre algorithme supervisé) ;
- entraînement du modèle sur le **jeu d’entraînement** ;
- première évaluation sur le jeu d’entraînement pour vérifier l’absence de problème majeur (erreur très forte, surapprentissage évident, etc.).

Le modèle entraîné est ensuite **sauvegardé** dans un fichier au format `.pkl`, ce qui permet de le recharger facilement sans devoir le réentraîner à chaque fois.

### 7.2. Script de prédiction

Un script séparé est dédié à la **prédiction** :

- chargement du modèle `.pkl` ;
- chargement ou préparation des données à prédire ;
- génération des **valeurs prédites** par le modèle.

Ce script permet de **réutiliser** le modèle sur de nouvelles données ou dans un autre contexte sans repasser par la phase d’entraînement.

---

## 8. Évaluation du modèle : MAE, RMSE, MAPE et analyse des erreurs

### 8.1. Indicateurs d’erreur

Pour mesurer la qualité des prédictions, plusieurs métriques ont été calculées sur le **jeu de test** :

- **MAE (Mean Absolute Error)** :  
  \- Valeur obtenue : **1,26**  
  \- Interprétation : en moyenne, l’écart absolu entre la valeur réelle et la valeur prédite est de 1,26 unité.  

- **RMSE (Root Mean Squared Error)** :  
  \- Valeur obtenue : **1,48**  
  \- Interprétation : cette métrique pénalise davantage les grosses erreurs. Sa valeur est proche du MAE, ce qui peut indiquer qu’il n’y a pas trop d’erreurs extrêmes.

- **MAPE (Mean Absolute Percentage Error)** :  
  \- Valeur obtenue : **66,74 %**  
  \- Interprétation : en moyenne, le modèle se trompe d’environ **67 %** par rapport aux valeurs réelles.

Concrètement, un MAPE de 66,74 % signifie que si la vraie valeur est 100, la prédiction moyenne peut être autour de 33 ou de 167.  
Cela montre que, **en termes relatifs**, le modèle reste **peu précis**, même si l’erreur absolue (MAE ≈ 1,26) peut paraître faible selon l’échelle de la variable cible.

Dans le cahier des charges, l’objectif pouvait être par exemple d’obtenir un **MAPE < 30 %**.  
Avec un MAPE de **66,74 %**, cet objectif **n’est pas atteint**, ce qui met en évidence des marges d’amélioration du modèle.

### 8.2. Graphique d’analyse des erreurs

Un **graphique d’analyse des erreurs** a été ajouté au projet.  
Ce graphique permet notamment de :

- visualiser les **écarts entre valeurs réelles et prédites** ;
- repérer les observations où l’erreur est particulièrement élevée ;
- analyser si le modèle a tendance à **sous-estimer** ou **surestimer** systématiquement dans certains cas.

Ce type de visualisation complète les métriques globales (MAE, RMSE, MAPE) en donnant une vue plus détaillée du comportement du modèle.

---

## 9. Bilan du projet

Ce projet a permis de :

1. **Construire une base de données MySQL** structurée pour stocker les ventes ;
2. **Charger et nettoyer** ces données dans Python (harmonisation des pays, préparation d’un dataset nettoyé) ;
3. Réaliser une **analyse exploratoire** des ventes (par pays, par canal), avec des visualisations claires ;
4. Mettre en place un **modèle de prédiction** des ventes et un script de prédiction réutilisable ;
5. **Évaluer** les performances du modèle à l’aide de plusieurs métriques (MAE, RMSE, MAPE) et d’un **graphique d’analyse des erreurs**.

Même si les résultats montrent un **MAPE relativement élevé (66,74 %)**, le travail réalisé illustre bien un pipeline typique de **data analyst / data scientist junior**, allant :

- de la base de données,
- à l’analyse exploratoire,
- jusqu’à la mise en place et l’évaluation d’un modèle prédictif.

---

## 10. Pistes d’amélioration

Plusieurs axes d’amélioration sont possibles :

- Tester différents **algorithmes de machine learning** (forêts aléatoires, gradient boosting, modèles non linéaires, etc.) et comparer leurs performances au modèle actuel ;
- Améliorer la **préparation des données** :
  - traitement plus avancé des valeurs manquantes ;
  - création de nouvelles variables (saisonnalité, effets calendaires, agrégations par période, etc.) ;
  - détection et traitement des **valeurs aberrantes** (outliers) qui peuvent fortement impacter le MAPE ;
- Mettre en place une **validation croisée** (`cross-validation`) pour obtenir une estimation plus robuste de la performance ;
- Affiner les hyperparamètres du modèle (tuning) pour tenter de réduire l’erreur ;
- Intégrer des **tableaux de bord** (par exemple avec un outil de BI ou une application web) pour rendre l’analyse accessible à des utilisateurs non techniques ;
- Automatiser tout le pipeline (exécution régulière des scripts, mise à jour automatique des prédictions à partir de la base MySQL).

---

## 11. Conclusion

Ce projet montre qu’il est possible, à partir de données de ventes brutes stockées dans une base MySQL, de :

- structurer les données dans une base relationnelle ;
- analyser les ventes de manière claire (par pays, par canal, etc.) ;
- entraîner un modèle de prédiction en Python ;
- et mesurer précisément la qualité de ce modèle grâce à plusieurs métriques (MAE, RMSE, MAPE) et à un graphique d’analyse des erreurs.

Même si le **MAPE de 66,74 %** indique que les prédictions restent encore approximatives, le pipeline mis en place constitue une **base solide** pour des analyses et prédictions de ventes plus avancées à l’avenir.

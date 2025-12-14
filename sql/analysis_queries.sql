-- 1. Afficher toutes les ventes
SELECT *
FROM vente_chanel;

-- 2. Afficher les ventes du produit Bleu de Chanel
SELECT *
FROM vente_chanel
WHERE produit = 'Bleu de Chanel';

-- 3. Nombre total de ventes
SELECT COUNT(*) AS nombre_de_ventes
FROM vente_chanel;

-- 4. Quantité totale vendue
-- Objectif : savoir combien d’unités ont été vendues
SELECT SUM(quantite) AS total_quantite_vendue
FROM vente_chanel;

-- 5. Chiffre d’affaires total
SELECT SUM(quantite * prix) AS chiffre_affaires_total
FROM vente_chanel;
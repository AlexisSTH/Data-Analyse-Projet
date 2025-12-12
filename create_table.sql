CREATE TABLE vente_chanel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produit VARCHAR(100) NOT NULL,
    date_vente DATE NOT NULL,
    quantite INT NOT NULL,
    prix DECIMAL(10,2) NOT NULL,
    pays VARCHAR(50),
    canal VARCHAR(50)
    );
CREATE DATABASE Products CHARACTER SET utf8mb4 COLLATE utf8mb4_turkish_ci;
use Products;

CREATE TABLE ProductTable (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_turkish_ci,
    image VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_turkish_ci,
    price FLOAT
);

SET NAMES utf8mb4 COLLATE utf8mb4_turkish_ci;

CREATE DATABASE IF NOT EXISTS super CHARACTER SET utf8mb4;
USE super;

CREATE TABLE IF NOT EXISTS productos (
    codigo  INT PRIMARY KEY,
    descrip VARCHAR(100) NOT NULL,
    stock   INT NOT NULL,
    precio  DECIMAL(10,2) NOT NULL,
    sector  VARCHAR(50),
    marca   VARCHAR(50),
    foto    VARCHAR(255)
);
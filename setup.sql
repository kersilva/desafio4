CREATE DATABASE IF NOT EXISTS notas
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE notas;

CREATE TABLE centrais (
    id         INT          AUTO_INCREMENT PRIMARY KEY,
    cd_central VARCHAR(8)   NOT NULL UNIQUE
);

CREATE TABLE notas (
    id               INT           AUTO_INCREMENT PRIMARY KEY,
    id_central       INT           NOT NULL,
    titulo           VARCHAR(50)   NOT NULL UNIQUE,
    texto            TEXT,
    data_criacao     DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao DATETIME      NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_central) REFERENCES centrais(id) ON DELETE CASCADE
);

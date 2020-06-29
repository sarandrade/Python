CREATE TABLE IF NOT EXISTS cidades (
    id int unsigned not null auto_increment,
    nome varchar(255) not null,
    estado_id int unsigned not null,
    area decimal(10,2),
    PRIMARY KEY (id),
    FOREIGN KEY (estado_id) REFERENCES estados (id)
);

CREATE TABLE IF NOT EXISTS teste (
    id int unsigned not null auto_increment PRIMARY KEY
);

DROP TABLE IF EXISTS teste;
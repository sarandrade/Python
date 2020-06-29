ALTER TABLE empresas MODIFY cnpj varchar(10);

insert into empresas
    (nome, cnpj)
values
    ('Bradesco', 5487596215),
    ('Vale', 5485596215),
    ('Cielo', 0487596215);

desc empresas; -- Descreve a Tabela
select * from empresas;
select * from cidades;

insert into empresas_unidades
    (empresa_id, cidade_id, sede)
values
    (1, 4, 1),
    (1, 1, 0),
    (2, 4, 0),
    (2, 1, 1);

select * from empresas_unidades;
-- Criando uma tabela simples de clientes
CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    cidade VARCHAR(50)
);

-- Inserindo dados de exemplo
INSERT INTO clientes (id, nome, cidade) VALUES (1, 'Leuvis', 'São Paulo');
INSERT INTO clientes (id, id, cidade) VALUES (2, 'Ana', 'Rio de Janeiro');

-- Fazendo uma consulta para buscar todos os clientes
SELECT * FROM clientes;

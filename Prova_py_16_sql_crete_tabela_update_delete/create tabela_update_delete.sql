-- Criar o banco de dados
CREATE DATABASE Infinity_School;

-- Usar o banco de dados criado
USE Infinity_School;

-- Criar a tabela "pessoas"
CREATE TABLE pessoas (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    nome_completo VARCHAR(100),
    idade INT,
    genero VARCHAR(10),
    nacionalidade VARCHAR(50),
    email VARCHAR(100),
    estado_civil VARCHAR(20),
    nome_pai VARCHAR(100),
    nome_mae VARCHAR(100)
);

-- Inserir registros de exemplo na tabela "pessoas"
INSERT INTO pessoas (nome_completo, idade, genero, nacionalidade, email, estado_civil, nome_pai, nome_mae) VALUES
('João Silva', 30, 'Masculino', 'Brasileiro', 'joao.silva@example.com', 'Solteiro', 'José Silva', 'Maria Silva'),
('Maria Santos', 25, 'Feminino', 'Portuguesa', 'maria.santos@example.com', 'Casado', 'Antônio Santos', 'Ana Santos'),
('Pedro Almeida', 35, 'Masculino', 'Brasileiro', 'pedro.almeida@example.com', 'Solteiro', 'Carlos Almeida', 'Marta Almeida'),
('Ana Oliveira', 28, 'Feminino', 'Brasileira', 'ana.oliveira@example.com', 'Divorciado', 'Fernando Oliveira', 'Carla Oliveira'),
('Luiz Costa', 40, 'Masculino', 'Brasileiro', 'luiz.costa@example.com', 'Casado', 'Ricardo Costa', 'Sônia Costa'),
('Mariana Rodrigues', 32, 'Feminino', 'Brasileira', 'mariana.rodrigues@example.com', 'Solteiro', 'Antônio Rodrigues', 'Sandra Rodrigues'),
('Paulo Santos', 45, 'Masculino', 'Brasileiro', 'paulo.santos@example.com', 'Casado', 'Joaquim Santos', 'Luciana Santos'),
('Fernanda Lima', 27, 'Feminino', 'Brasileira', 'fernanda.lima@example.com', 'Solteiro', 'Roberto Lima', 'Alice Lima'),
('Gustavo Pereira', 33, 'Masculino', 'Brasileiro', 'gustavo.pereira@example.com', 'Divorciado', 'Carlos Pereira', 'Patrícia Pereira'),
('Camila Oliveira', 29, 'Feminino', 'Brasileira', 'camila.oliveira@example.com', 'Casado', 'Ricardo Oliveira', 'Fernanda Oliveira');

SELECT * FROM pessoas;

-- Modificar informações do registro com ID 3
UPDATE pessoas
SET nome_completo = 'Carla Almeida',
    idade = 36,
    nacionalidade = 'Brasileira',
    email = 'carla.almeida@example.com',
    estado_civil = 'Casada',
    nome_pai = 'Carlos Almeida',
    nome_mae = 'Marta Almeida'
WHERE ID = 3;

-- Remover o registro com ID 7
DELETE FROM pessoas
WHERE ID = 7;

SELECT * FROM pessoas;


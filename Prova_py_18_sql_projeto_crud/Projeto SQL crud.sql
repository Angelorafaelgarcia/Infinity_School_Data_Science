CREATE DATABASE livraria;
USE livraria;

CREATE TABLE livros(
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255),
    genero VARCHAR(255),
    autor VARCHAR(255) NOT NULL,
    ano_publicacao int
);

CREATE TABLE cliente(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    cpf varchar (14),
    email varchar (255)
);

INSERT INTO livros VALUES(
	DEFAULT,
    "Codigo Limpo",
    "Tecnologia",
    "Robert C. Martin",
    "2009"
);

INSERT INTO livros VALUES(
	DEFAULT,
    "O Codificador Limpo",
    "Tecnologia",
    "Bob Martin",
    "2012"
);

INSERT INTO livros VALUES(
	DEFAULT,
    "O Programador Pragmatico: De aprendiz a mestre",
    "Tecnologia",
    "Andrew Hunt",
    "2010"
);

INSERT INTO livros VALUES(
	DEFAULT,
    "Padrões de Projetos: Soluções Reutilizáveis de Software Orientados a Objetos",
    "Tecnologia",
    "Erich Gamma",
    "2000"
);

INSERT INTO livros VALUES(
	DEFAULT,
    "Arquitetura limpa: O guia do artesão para estrutura e design de software",
    "Tecnologia",
    "Robert C. Martin",
    "2019"
);

select * from livros





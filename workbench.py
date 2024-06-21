-- Posso realizar comentários no meu script;

-- Criação do arquivo de banco de dados se não existir;
CREATE DATABASE IF NOT EXISTS banco_de_dados;
CREATE DATABASE IF NOT EXISTS banco_de_dados2;

-- Especificar qual banco de dados estou usando;
USE banco_de_dados;

-- Criar uma tabela no banco de dados usado;
CREATE TABLE IF NOT EXISTS  usuarios (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
senha VARCHAR (255) NOT NULL,
data_de_nascimento DATE,
criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);





-- Criação da tabela de perfis;
CREATE TABLE IF NOT EXISTS perfis(
id INT AUTO_INCREMENT PRIMARY KEY,
usuario_id INT NOT NULL,
bio TEXT,
avatar_url VARCHAR(255),
criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
CONSTRAINT fk_usuario FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Inserção dados em minha tabela "usuario";

-- Determino qual arquivo de BD estou ultilizando para realizar algo
USE banco_de_dados;

-- Inserir os dados na tabela 'usuarios'
INSERT INTO usuarios (nome, email, senha, data_nascimento) VALUES
('Presidente', 'presidentejunior@gmail.com', '123_presidencia', 1970-01-01),
('Widley', 'eusouwidley@gmail.com', ' meu_nome_widley123', '1999-15-12');

-- Inserir dados na tabela 'perfis'
INSERT INTO perfis (usuario_id, bio, avatar_url) VALUES
(1,'Desenvolvedor Full-Stack Sênior do Google, tão rico que dá desespero', 'https://exemplodefoto.com.br'),
(2,'Gerente de projetos da Tesla', 'https://teslafotosdowidley.com');

-- Exemplo de atualização de dados

UPDATE usuarios
SET
	nome = 'José Júnior',
    email = 'expresidentejunior@gmail.com'
WHERE
	id = 1;
    
-- Exemplo de como visualizar se a atualização foi feita

SELECT * FROM usuarios WHERE id = 1 



CREATE DATABASE IF NOT EXISTS banco_de_dados2;
USE banco_de_dados2;

CREATE TABLE IF NOT EXISTS item_estoque(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100) NOT NULL,
marca VARCHAR(30) NOT NULL,
preço NUMERIC(10, 2) NOT NULL,
modelo VARCHAR(30) NOT NULL,
quantidade NUMERIC
);

INSERT INTO item_estoque (nome, marca, preço, modelo, quantidade) VALUES('Gustavo', 'Armani' ,500.50,'Camisa' ,15 );

UPDATE item_estoque
SET 
	
    preço = 1500.00
    
WHERE
	id = 1;
    
SELECT * FROM item_estoque WHERE id = 1;

CREATE DATABASE IF NOT EXISTS Livraria;

USE livraria;

CREATE TABLE if not exists Livro(
id int primary key auto_increment,
nome_livro VARCHAR(50),
nome_autor varchar(50),
sexo_autor CHAR(1),
numero_paginas INTEGER(4),
nome_editora VARCHAR(50),
valor_livro DECIMAL (10,2),
uf_editora CHAR(2),
ano_publicacao INTEGER (4)
);

INSERT INTO livro(nome_livro, nome_autor, sexo_autor, numero_paginas, nome_editora, valor_livro, uf_editora, ano_publicacao) VALUES ('Cavaleiro Real', 'Ana Claudia', 'F', 450, 'Atlas', 49.90, 'RJ', 2009),
INSERT INTO livro(nome_livro, nome_autor, sexo_autor, numero_paginas, nome_editora, valor_livro, uf_editora, ano_publicacao) VALUES ('SQL para leigos', 'João Nunes', 'M', 210, 'Addison', 45, 'SP', 2018),
INSERT INTO livro(nome_livro, nome_autor, sexo_autor, numero_paginas, nome_editora, valor_livro, uf_editora, ano_publicacao) VALUES ('Pessoas efetivas', 'Eduardo Santos', 'M', 390, 'Beta', 78.99, 'RJ', 2008),
INSERT INTO livro(nome_livro, nome_autor, sexo_autor, numero_paginas, nome_editora, valor_livro, uf_editora, ano_publicacao) VALUES ('Receitas caseiras', 'Célia Tavares', 'F', 210, 'Atlas', 78.99, 'RJ', 2018),
INSERT INTO livro(nome_livro, nome_autor, sexo_autor, numero_paginas, nome_editora, valor_livro, uf_editora, ano_publicacao) VALUES ('Hábitos Saudáveis ', 'Eduardo Santos', 'M', 630, 'Beta', 150.98, 'RJ', 2019),
INSERT INTO livro(nome_livro, nome_autor, sexo_autor, numero_paginas, nome_editora, valor_livro, uf_editora, ano_publicacao) VALUES ('A casa marrom', 'Hermes Macedo', 'M', 250, 'Bubba', 60, 'RJ', 2016),
INSERT INTO livro(nome_livro, nome_autor, sexo_autor, numero_paginas, nome_editora, valor_livro, uf_editora, ano_publicacao) VALUES ('Estácio querido', 'Geraldo Francisco', 'M', 310, 'Insignia', 100, 'MG', 2015),
INSERT INTO livro(nome_livro, nome_autor, sexo_autor, numero_paginas, nome_editora, valor_livro, uf_editora, ano_publicacao) VALUES ('Para sempre amigas', 'Leda Silva', 'F', 510, 'Insignia', 78.98, 'ES', 2011),
INSERT INTO livro(nome_livro, nome_autor, sexo_autor, numero_paginas, nome_editora, valor_livro, uf_editora, ano_publicacao) VALUES ('Copas inesqueciveis', 'Marco Alcantara', 'M', 200, 'Larson', 130.98, 'RS', 2018),
INSERT INTO livro(nome_livro, nome_autor, sexo_autor, numero_paginas, nome_editora, valor_livro, uf_editora, ano_publicacao) VALUES ('O poder da mente', 'Clara Mafra', 'F', 120, 'Continental', 56.58, 'RS', 2017);

-- Questao 1
SELECT * FROM livro ;

-- Questao 2
SELECT nome_livro, nome_editora FROM livro ; 

-- Questao 3
SELECT nome_livro, uf_editora FROM livro WHERE sexo_autor = 'M';

-- Questão 4
SELECT nome_livro, numero_paginas FROM livro WHERE sexo_autor = ' F';

-- Questão 5 
SELECT valor_livro FROM livro WHERE uf_editora = 'SP';

-- Questao 6
SELECT nome_autor, sexo_autor FROM livro WHERE sexp_autor = 'M' AND (uf_editora = 'RJ' OR uf_editora = 'SP');


 

CREATE DATABASE IF NOT EXISTS Loja;

USE Loja;

CREATE TABLE IF NOT EXISTS clientes(
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,  
nome VARCHAR(50) NOT NULL,
cpf CHAR(11) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS compras(
id INT AUTO_INCREMENT PRIMARY KEY,
data_compra DATE not null,
id_cliente INT not null,

FOREIGN KEY (id_cliente) REFERENCES clientes(id)

);

CREATE TABLE IF NOT EXISTS produtos(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50) NOT NULL,
descricao VARCHAR(255),
preco DECIMAL(10,2) NOT NULL

);

CREATE TABLE IF NOT EXISTS compras_produtos(
id_compra INT NOT NULL,
id_produto INT NOT NULL,
quantidade INT NOT NULL,

PRIMARY KEY (id_compra, id_produto),

FOREIGN kEY (id_compra) REFERENCES compras(id),
FOREIGN kEY (id_produto) REFERENCES produtos(id)

);

USE Loja;

INSERT INTO clientes (nome, cpf) VALUES ('Naruto', '12345678900');
INSERT INTO clientes (nome, cpf) VALUES ('Rock Lee', '32165489700'); 
INSERT INTO clientes (nome, cpf) VALUES ('Goku', '45678912300');
INSERT INTO clientes (nome, cpf) VALUES ('Yugi', '78912345688');  
INSERT INTO clientes (nome, cpf) VALUES ('Ash', '56789412566');
 
INSERT INTO compras (data_compra, id_cliente) VALUES ('2024-06-17',1);
INSERT INTO compras (data_compra, id_cliente) VALUES ('2024-06-18',1);
INSERT INTO compras (data_compra, id_cliente) VALUES ('2024-06-19',3);
INSERT INTO compras (data_compra, id_cliente) VALUES ('2024-06-20',5);

INSERT INTO produtos (nome, descricao, preco) VALUES ('celular', 'android', 1000);
INSERT INTO produtos (nome, descricao, preco) VALUES ('Pc', 'Windows', 1500);
INSERT INTO produtos (nome, descricao, preco) VALUES ('Cadeira Gamer', 'Ergonômica', 700);
INSERT INTO produtos (nome, descricao, preco) VALUES ('Teclado Mecânico', 'Mancer', 150);
INSERT INTO produtos (nome, descricao, preco) VALUES ('Notebook', 'DELL', 3000);
INSERT INTO produtos (nome, descricao, preco) VALUES ('Mouse gamer', 'Redragon', 150);

INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 1, 1, 5);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 1, 2, 2);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 2, 4, 7);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 2, 6, 3);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 2, 3, 4);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 3, 3, 2);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 4, 5, 5);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 4, 2, 1);

CREATE DATABASE IF NOT EXISTS Loja;

USE Loja;

CREATE TABLE IF NOT EXISTS clientes(
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,  
nome VARCHAR(50) NOT NULL,
cpf CHAR(11) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS compras(
id INT AUTO_INCREMENT PRIMARY KEY,
data_compra DATE not null,
id_cliente INT not null,

FOREIGN KEY (id_cliente) REFERENCES clientes(id)

);

CREATE TABLE IF NOT EXISTS produtos(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50) NOT NULL,
descricao VARCHAR(255),
preco DECIMAL(10,2) NOT NULL

);

CREATE TABLE IF NOT EXISTS compras_produtos(
id_compra INT NOT NULL,
id_produto INT NOT NULL,
quantidade INT NOT NULL,

PRIMARY KEY (id_compra, id_produto),

FOREIGN kEY (id_compra) REFERENCES compras(id),
FOREIGN kEY (id_produto) REFERENCES produtos(id)

);

INSERT INTO clientes (nome, cpf) VALUES ('Naruto', '12345678900');
INSERT INTO clientes (nome, cpf) VALUES ('Rock Lee', '32165489700'); 
INSERT INTO clientes (nome, cpf) VALUES ('Goku', '45678912300');
INSERT INTO clientes (nome, cpf) VALUES ('Yugi', '78912345688');  
INSERT INTO clientes (nome, cpf) VALUES ('Ash', '56789412566');
 
INSERT INTO compras (data_compra, id_cliente) VALUES ('2024-06-17',1);
INSERT INTO compras (data_compra, id_cliente) VALUES ('2024-06-18',1);
INSERT INTO compras (data_compra, id_cliente) VALUES ('2024-06-19',3);
INSERT INTO compras (data_compra, id_cliente) VALUES ('2024-06-20',5);

INSERT INTO produtos (nome, descricao, preco) VALUES ('celular', 'android', 1000);
INSERT INTO produtos (nome, descricao, preco) VALUES ('Pc', 'Windows', 1500);
INSERT INTO produtos (nome, descricao, preco) VALUES ('Cadeira Gamer', 'Ergonômica', 700);
INSERT INTO produtos (nome, descricao, preco) VALUES ('Teclado Mecânico', 'Mancer', 150);
INSERT INTO produtos (nome, descricao, preco) VALUES ('Notebook', 'DELL', 3000);
INSERT INTO produtos (nome, descricao, preco) VALUES ('Mouse gamer', 'Redragon', 150);

INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 1, 1, 5);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 1, 2, 2);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 2, 4, 7);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 2, 6, 3);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 2, 3, 4);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 3, 3, 2);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 4, 5, 5);
INSERT INTO compras_produtos (id_compra, id_produto, quantidade) VALUES ( 4, 2, 1);

SELECT compras_produtos.id_compra, produtos.nome, compras_produtos.quantidade
FROM produtos, compras_produtos
WHERE produtos.id = compras.id_produto;

SELECT P.nome, CP.quantidade, CO.data


CREATE DATABASE IF NOT EXISTS videolocadora;

USE videolocadora;

CREATE TABLE IF NOT EXISTS filmes(
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    diretor VARCHAR(255) NOT NULL,
    ano INT NOT NULL,
    genero VARCHAR(255) NOT NULL
	);

INSERT INTO filmes (titulo, diretor, ano, genero) VALUES ("Impacto Profundo", "Arnold", 1987, "Ação");
INSERT INTO filmes (titulo, diretor, ano, genero) VALUES ("Matrix", "Neo", 1999, "Ficção");

SELECT * FROM filmes;

UPDATE filmes SET titulo = "A Procura de um Milagre" WHERE titulo = "Impacto Profundo";

DELETE FROM filmes WHERE titulo = "Matrix";

-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 10/06/2024 às 21:49
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `projeto_site`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nome_completo` varchar(100) NOT NULL,
  `cpf` varchar(14) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `telefone` varchar(15) NOT NULL,
  `data_nascimento` text NOT NULL,
  `genero` varchar(10) NOT NULL,
  `caminho_curriculo` varchar(255) DEFAULT NULL,
  `experiencia_antecessora` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `nome_completo`, `cpf`, `senha`, `telefone`, `data_nascimento`, `genero`, `caminho_curriculo`, `experiencia_antecessora`) VALUES
(13, 'dayvissom', '121.232.574-00', 'aa', '(99) 99999-9999', '08/04/2003', 'Masculino', NULL, 'sfasda'),
(14, 'dayvissom', '121.232.574-11', 'a', '(99) 99999-9999', '08/04/2003', 'Masculino', NULL, 'sfasda');

-- --------------------------------------------------------

--
-- Estrutura para tabela `vagas`
--

CREATE TABLE `vagas` (
  `id` int(11) NOT NULL,
  `nome` text DEFAULT NULL,
  `tipo` text DEFAULT NULL,
  `salario` text DEFAULT NULL,
  `quantidade_vagas` text DEFAULT NULL,
  `escolaridade` text DEFAULT NULL,
  `disponibilidade` text DEFAULT NULL,
  `localidade` text DEFAULT NULL,
  `carga_horaria` text DEFAULT NULL,
  `descricao_vaga` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `vagas`
--

INSERT INTO `vagas` (`id`, `nome`, `tipo`, `salario`, `quantidade_vagas`, `escolaridade`, `disponibilidade`, `localidade`, `carga_horaria`, `descricao_vaga`) VALUES
(9, 'VAGA', 'vaga', '1.200,00', '3 vagas', 'Ensino medio', '1 as 2', 'Arapiraca - AL', '8 horas', 'asasas');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `vagas`
--
ALTER TABLE `vagas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de tabela `vagas`
--
ALTER TABLE `vagas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


CREATE DATABASE IF NOT EXISTS lojadiscos;

USE lojadiscos;

CREATE TABLE IF NOT EXISTS disco(
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    artista VARCHAR(255) NOT NULL,
    ano INT NOT NULL,
    genero VARCHAR(255) NOT NULL,
    esta_alugado TINYINT(1) DEFAULT 0
);

INSERT INTO disco (titulo, artista, ano, genero, esta_alugado) VALUES ("Maquina do tempo", "Matue", 2022, "Trap", "1");
INSERT INTO disco (titulo, artista, ano, genero, esta_alugado) VALUES ("Languange", "Sidoka", 2020, "Trap", "0");

SELECT * FROM disco;

-- Selects

SELECT SUM(cp.quantidade)
FROM produtos as P
	INNER JOIN compras_produto as CP
    ON P.id = CP.id_produto
GROUP BY p.id;
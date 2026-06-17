-- =====================================================
-- DataShop - Modelagem de Banco de Dados E-commerce
-- Criação das tabelas e relacionamentos
-- =====================================================

-- Tabela de clientes
CREATE TABLE clientes (
    id_cliente  SERIAL PRIMARY KEY,
    nome        VARCHAR(100) NOT NULL,
    email       VARCHAR(100) UNIQUE,
    cidade      VARCHAR(50),
    estado      VARCHAR(2)
);

-- Tabela de vendedores
CREATE TABLE vendedores (
    id_vendedor  SERIAL PRIMARY KEY,
    nome         VARCHAR(100) NOT NULL,
    regiao       VARCHAR(20),
    email        VARCHAR(100) UNIQUE
);

-- Tabela de produtos
CREATE TABLE produtos (
    id_produto   SERIAL PRIMARY KEY,
    nome         VARCHAR(100) NOT NULL,
    categoria    VARCHAR(50),
    preco        DECIMAL(10,2) NOT NULL,
    estoque      INTEGER DEFAULT 0
);

-- Tabela de pedidos (conecta clientes e vendedores)
CREATE TABLE pedidos (
    id_pedido    SERIAL PRIMARY KEY,
    id_cliente   INTEGER REFERENCES clientes(id_cliente),
    id_vendedor  INTEGER REFERENCES vendedores(id_vendedor),
    data_pedido  DATE NOT NULL,
    status       VARCHAR(20) DEFAULT 'pendente'
);

-- Tabela de itens do pedido (conecta pedidos e produtos)
-- Resolve o relacionamento "muitos para muitos"
CREATE TABLE itens_pedido (
    id_item          SERIAL PRIMARY KEY,
    id_pedido        INTEGER REFERENCES pedidos(id_pedido),
    id_produto       INTEGER REFERENCES produtos(id_produto),
    quantidade       INTEGER NOT NULL,
    preco_unitario   DECIMAL(10,2) NOT NULL
);
-- =====================================================
-- DataShop - Inserção de Dados de Exemplo
-- =====================================================

-- Clientes
INSERT INTO clientes (nome, email, cidade, estado) VALUES
('Ana Silva',    'ana@email.com',    'São Paulo',    'SP'),
('Bruno Costa',  'bruno@email.com',  'Curitiba',     'PR'),
('Carla Souza',  'carla@email.com',  'Recife',       'PE'),
('Diego Lima',   'diego@email.com',  'Manaus',       'AM'),
('Elena Santos', 'elena@email.com',  'Porto Alegre', 'RS');

-- Vendedores
INSERT INTO vendedores (nome, regiao, email) VALUES
('Marcos Oliveira', 'Sudeste',  'marcos@datashop.com'),
('Julia Ferreira',  'Sul',      'julia@datashop.com'),
('Pedro Alves',     'Nordeste', 'pedro@datashop.com');

-- Produtos
INSERT INTO produtos (nome, categoria, preco, estoque) VALUES
('Notebook Dell',    'Eletrônicos', 3500.00, 15),
('Mouse Logitech',   'Periféricos',  150.00, 80),
('Monitor LG',       'Eletrônicos', 1200.00, 20),
('Teclado Mecânico', 'Periféricos',  350.00, 45),
('SSD Samsung',      'Componentes',  400.00, 60),
('Webcam Logitech',  'Periféricos',  280.00, 35);

-- Pedidos
-- Observação: os IDs abaixo correspondem à ordem de inserção acima.
-- Se você rodar esse script do zero em um banco novo, os IDs vão começar em 1.
INSERT INTO pedidos (id_cliente, id_vendedor, data_pedido, status) VALUES
(1, 1, '2024-01-05', 'entregue'),
(2, 2, '2024-01-06', 'entregue'),
(3, 3, '2024-01-07', 'enviado'),
(4, 1, '2024-01-08', 'pendente'),
(5, 2, '2024-01-09', 'entregue');

-- Itens dos pedidos
INSERT INTO itens_pedido (id_pedido, id_produto, quantidade, preco_unitario) VALUES
(1, 1, 1, 3500.00),
(1, 2, 2,  150.00),
(2, 3, 1, 1200.00),
(2, 4, 1,  350.00),
(3, 5, 2,  400.00),
(4, 6, 1,  280.00),
(5, 1, 1, 3500.00),
(5, 2, 3,  150.00);
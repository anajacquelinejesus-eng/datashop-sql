-- =====================================================
-- DataShop - Queries de Análise de Negócio
-- =====================================================

-- 1. Relatório completo de vendas (cliente, vendedor, produto)
SELECT
    c.nome          AS cliente,
    v.nome          AS vendedor,
    p.nome          AS produto,
    i.quantidade,
    i.preco_unitario,
    i.quantidade * i.preco_unitario AS total_item,
    pe.status,
    pe.data_pedido
FROM pedidos pe
JOIN clientes      c ON pe.id_cliente  = c.id_cliente
JOIN vendedores    v ON pe.id_vendedor = v.id_vendedor
JOIN itens_pedido  i ON pe.id_pedido   = i.id_pedido
JOIN produtos      p ON i.id_produto   = p.id_produto
ORDER BY pe.data_pedido, cliente;


-- 2. Qual vendedor gerou mais receita?
SELECT
    v.nome AS vendedor,
    SUM(i.quantidade * i.preco_unitario) AS receita_total
FROM vendedores v
JOIN pedidos pe     ON pe.id_vendedor = v.id_vendedor
JOIN itens_pedido i ON i.id_pedido    = pe.id_pedido
GROUP BY v.nome
ORDER BY receita_total DESC;


-- 3. Qual cliente gastou mais no total?
SELECT
    c.nome AS cliente,
    SUM(i.quantidade * i.preco_unitario) AS receita_total
FROM clientes c
JOIN pedidos pe     ON pe.id_cliente = c.id_cliente
JOIN itens_pedido i ON i.id_pedido   = pe.id_pedido
GROUP BY c.nome
ORDER BY receita_total DESC;


-- 4. Pedidos pendentes ou enviados (ainda não entregues)
SELECT
    c.nome   AS cliente,
    v.nome   AS vendedor,
    p.status
FROM clientes c
JOIN pedidos p    ON p.id_cliente  = c.id_cliente
JOIN vendedores v ON v.id_vendedor = p.id_vendedor
WHERE p.status IN ('pendente', 'enviado');


-- 5. Ranking de produtos mais vendidos por quantidade
SELECT
    pr.nome AS produto,
    SUM(i.quantidade) AS total_vendido
FROM produtos pr
JOIN itens_pedido i ON i.id_produto = pr.id_produto
GROUP BY pr.nome
ORDER BY total_vendido DESC;
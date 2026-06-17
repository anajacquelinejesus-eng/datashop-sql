# 🛍️ DataShop SQL — Modelagem e Análise de Dados de E-commerce

Projeto de modelagem relacional e análise de dados usando SQL puro, simulando o banco de dados de um e-commerce fictício chamado DataShop.

## 📌 Sobre o projeto

Este projeto demonstra a construção de um banco de dados relacional do zero, incluindo modelagem de entidades, relacionamentos com chaves estrangeiras, inserção de dados e queries analíticas para responder perguntas reais de negócio.

## 🗂️ Estrutura do banco de dados

O banco simula um e-commerce com 5 entidades principais:

- **clientes** — pessoas que fazem pedidos
- **vendedores** — responsáveis pelos pedidos
- **produtos** — itens disponíveis para venda
- **pedidos** — registra cada compra (conecta cliente e vendedor)
- **itens_pedido** — produtos dentro de cada pedido (relação muitos-para-muitos)

## 🔗 Diagrama de relacionamento
clientes ──┐

├── pedidos ──── itens_pedido ──── produtos

vendedores─┘

## 📁 Organização dos arquivos

| Arquivo | Descrição |
|---------|-----------|
| `sql/01_criar_tabelas.sql` | Criação das 5 tabelas com chaves primárias e estrangeiras |
| `sql/02_inserir_dados.sql` | Inserção de dados de exemplo |
| `sql/03_queries_analise.sql` | 5 queries respondendo perguntas de negócio |

## 📊 Perguntas de negócio respondidas

1. Quais produtos, vendedores e clientes formam o histórico completo de vendas?
2. Qual vendedor gerou mais receita?
3. Qual cliente gastou mais no total?
4. Quais pedidos ainda não foram entregues?
5. Quais produtos são mais vendidos em quantidade?

## 🛠️ Tecnologias utilizadas

- PostgreSQL
- SQL (DDL, DML, JOINs, agregações)

## 🚀 Como executar

1. Crie um banco de dados PostgreSQL
2. Execute os arquivos na ordem:
01_criar_tabelas.sql

02_inserir_dados.sql

03_queries_analise.sql

## 📈 Próximos passos

- Adicionar orquestração com Apache Airflow
- Containerizar o ambiente com Docker
- Criar dashboard de visualização dos dados

---

Projeto desenvolvido como parte da minha transição de carreira para Engenharia de Dados.
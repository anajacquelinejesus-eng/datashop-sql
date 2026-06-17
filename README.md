# 🛍️ DataShop SQL & ETL — Modelagem e Pipeline de Dados de E-commerce

Projeto de modelagem relacional, análise SQL e pipeline ETL em Python, simulando o banco de dados de um e-commerce fictício chamado DataShop.

## 📌 Sobre o projeto

Este projeto demonstra duas etapas complementares da engenharia de dados:

1. **Modelagem e análise** — construção de um banco relacional do zero, com chaves estrangeiras e queries analíticas (SQL puro)
2. **Pipeline ETL** — automação da extração, limpeza e carga de dados usando Python e Pandas

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
| `python/06_pandas_intro.py` | Introdução à exploração de dados com Pandas |
| `python/07_limpeza_dados.py` | Limpeza de dados: duplicatas, nulos e espaços extras |
| `python/09_etl_completo.py` | Pipeline ETL completo: Extract, Transform, Load |

## 🔄 Pipeline ETL

O pipeline lê um arquivo CSV simulando novos pedidos recebidos diariamente, identifica e corrige problemas comuns de dados reais, e carrega os dados limpos no PostgreSQL:

**Extract** → Lê o CSV `pedidos_novos.csv` com Pandas
**Transform** → Remove duplicatas, espaços em branco e preenche valores nulos
**Load** → Insere os dados limpos na tabela `vendas` do PostgreSQL

## 📊 Perguntas de negócio respondidas (SQL)

1. Quais produtos, vendedores e clientes formam o histórico completo de vendas?
2. Qual vendedor gerou mais receita?
3. Qual cliente gastou mais no total?
4. Quais pedidos ainda não foram entregues?
5. Quais produtos são mais vendidos em quantidade?

## 🛠️ Tecnologias utilizadas

- PostgreSQL
- SQL (DDL, DML, JOINs, agregações, CTEs, Window Functions)
- Python (Pandas, psycopg2, python-dotenv)

## 🚀 Como executar

### Banco de dados
1. Crie um banco de dados PostgreSQL
2. Execute os arquivos `sql/` na ordem numérica

### Pipeline ETL
1. Crie um arquivo `.env` na raiz do projeto com suas credenciais:
DB_HOST=localhost

DB_NAME=loja

DB_USER=postgres

DB_PASSWORD=sua_senha

DB_PORT=5432
2. Instale as dependências:
pip install pandas psycopg2-binary python-dotenv
3. Execute o pipeline:
python python/09_etl_completo.py

## 📈 Próximos passos

- Orquestrar o pipeline com Apache Airflow
- Containerizar o ambiente com Docker
- Criar testes automatizados para validar a qualidade dos dados

---

Projeto desenvolvido como parte da minha transição de carreira para Engenharia de Dados.
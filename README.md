## 📌 Sobre o projeto

Este projeto cobre o ciclo completo de engenharia de dados:

1. **Modelagem relacional** — banco de dados do zero com chaves estrangeiras e queries analíticas
2. **Pipeline ETL** — extração, limpeza e carga de dados com Python e Pandas
3. **Containerização** — ambiente reproduzível com Docker e Docker Compose
4. **Orquestração** — pipeline agendado e monitorado com Apache Airflow

## 🗂️ Estrutura do banco de dados

O banco simula um e-commerce com 5 entidades:

- **clientes** — pessoas que fazem pedidos
- **vendedores** — responsáveis pelos pedidos
- **produtos** — itens disponíveis para venda
- **pedidos** — registra cada compra (conecta cliente e vendedor)
- **itens_pedido** — produtos dentro de cada pedido (muitos-para-muitos)
clientes ──┐
├── pedidos ──── itens_pedido ──── produtos
vendedores─┘

## 📁 Organização dos arquivos

| Arquivo | Descrição |
|---------|-----------|
| `sql/01_criar_tabelas.sql` | Criação das 5 tabelas com PKs e FKs |
| `sql/02_inserir_dados.sql` | Inserção de dados de exemplo |
| `sql/03_queries_analise.sql` | 5 queries respondendo perguntas de negócio |
| `python/09_etl_completo.py` | Pipeline ETL: Extract, Transform, Load |
| `python/10_etl_pratica.py` | Segundo pipeline ETL desenvolvido de forma independente |
| `dags/dag_datashop.py` | DAG do Airflow orquestrando o pipeline ETL |
| `docker-compose.yml` | PostgreSQL containerizado com volume persistente |
| `docker-compose-airflow.yaml` | Stack completa do Airflow (webserver, scheduler, worker) |

## 🔄 Pipeline ETL

O pipeline lê um arquivo CSV simulando pedidos recebidos diariamente, corrige problemas comuns de dados reais, e carrega os dados limpos no PostgreSQL:

- **Extract** → Lê `pedidos_novos.csv` com Pandas
- **Transform** → Remove duplicatas, trata valores nulos e limpa espaços extras
- **Load** → Insere os dados limpos na tabela `vendas` do PostgreSQL

## 🤖 Orquestração com Airflow

O pipeline é orquestrado pelo Apache Airflow, rodando automaticamente todo dia via DAG:

```python
extrair_task >> transformar_task >> carregar_task
```

A interface web do Airflow (porta 8080) permite monitorar cada execução, ver logs detalhados e reprocessar dados em caso de falha.

## 📊 Perguntas de negócio respondidas (SQL)

1. Histórico completo de vendas (cliente, vendedor, produto)
2. Qual vendedor gerou mais receita?
3. Qual cliente gastou mais no total?
4. Quais pedidos ainda não foram entregues?
5. Quais produtos são mais vendidos em quantidade?

## 🛠️ Tecnologias utilizadas

- **PostgreSQL** — banco de dados relacional
- **SQL** — DDL, DML, JOINs, CTEs, Window Functions, subqueries
- **Python** — Pandas, psycopg2, python-dotenv
- **Docker + Docker Compose** — containerização e reprodutibilidade
- **Apache Airflow** — orquestração e agendamento de pipelines

## 🚀 Como executar

### Banco de dados (Docker)
```bash
docker compose up -d
```

### Pipeline ETL manual
```bash
# Crie o arquivo .env com suas credenciais
cp .env.example .env

# Instale as dependências
pip install pandas psycopg2-binary python-dotenv

# Execute
python python/09_etl_completo.py
```

### Airflow (orquestração automática)
```bash
# Inicializar
docker compose -f docker-compose-airflow.yaml up airflow-init

# Subir todos os serviços
docker compose -f docker-compose-airflow.yaml up -d

# Acessar interface: http://localhost:8080
# Login: airflow / airflow
```

---

Projeto desenvolvido como parte da minha transição de carreira para Engenharia de Dados.
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Extract
print("Extraindo dados do CSV...")
df = pd.read_csv("python/pedidos_fevereiro.csv")

# Transform
print("Limpando os dados...")
print("--- dados originais ---")
print(df)
print("total de linhas:", len(df))

# PROBELMA 1: Remover linhas duplicadas
df = df.drop_duplicates()

# PROBLEMA 2: Remove valores nulos na coluna "valor" 
df = df.dropna(subset=["valor"])

# PROBLEMA 3: Remover espaços extras na coluna "categoria"
df["categoria"] = df["categoria"].str.strip()

print("\n--- dados depois da limpeza ---")
print(df)
print("total de linhas:", len(df))

# Load
print("Conectando ao banco de dados...")

# Monta a string de conexão usando variáveis de ambiente, não valores fixos
string_conexao = (
    f"host={os.getenv('DB_HOST')} "
    f"dbname={os.getenv('DB_NAME')} "
    f"user={os.getenv('DB_USER')} "
    f"password={os.getenv('DB_PASSWORD')} "
    f"port={os.getenv('DB_PORT')}"
)   
conexao = psycopg2.connect(string_conexao)
cursor = conexao.cursor()
print("Inserindo dados na tabela vendas...")
for index, linha in df.iterrows():
    cursor.execute(
        """
        INSERT INTO vendas (produto, categoria, valor, data_venda, regiao)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (linha["produto"], linha["categoria"], linha["valor"], linha["data_venda"], linha["regiao"])
    )
conexao.commit()
cursor.close()
conexao.close()
print("ETL concluído! Dados inseridos com sucesso.")


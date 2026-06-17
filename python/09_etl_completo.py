import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# ===== EXTRACT =====
print("Extraindo dados do CSV...")
df = pd.read_csv("python/pedidos_novos.csv")


# ===== TRANSFORM =====
print("Limpando os dados...")
df["email"] = df["email"].str.strip()
df = df.drop_duplicates()
df["quantidade"] = df["quantidade"].fillna(1)

print(df)


# ===== LOAD =====
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
        (linha["produto"], "Diversos", linha["preco_unitario"], linha["data_pedido"], "Online")
    )

conexao.commit()
cursor.close()
conexao.close()

print("ETL concluído! Dados inseridos com sucesso.")
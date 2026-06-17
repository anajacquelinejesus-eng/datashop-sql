import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

string_conexao = (
    f"host={os.getenv('DB_HOST')} "
    f"dbname={os.getenv('DB_NAME')} "
    f"user={os.getenv('DB_USER')} "
    f"password={os.getenv('DB_PASSWORD')} "
    f"port={os.getenv('DB_PORT')}"
)

conexao = psycopg2.connect(string_conexao)

print("Conexão realizada com sucesso!")

conexao.close()
print("Conexão fechada.")
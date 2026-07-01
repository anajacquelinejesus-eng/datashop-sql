from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2

def extrair():
    df = pd.read_csv("/opt/airflow/python/pedidos_novos.csv")
    print(f"Extraídas {len(df)} linhas do CSV")
    return df.to_json()

def transformar(**context):
    from io import StringIO
    df_json = context["ti"].xcom_pull(task_ids="extrair_csv")
    df = pd.read_json(StringIO(df_json))
    df["email"] = df["email"].str.strip()
    df = df.drop_duplicates()
    df["quantidade"] = df["quantidade"].fillna(1)
    print(f"Dados limpos: {len(df)} linhas")
    return df.to_json()

def carregar(**context):
    from io import StringIO
    df_json = context["ti"].xcom_pull(task_ids="limpar_dados")
    df = pd.read_json(StringIO(df_json))
    conexao = psycopg2.connect(
        host="host.docker.internal",
        dbname="loja",
        user="postgres",
        password="112002",
        port=5432
    )
    cursor = conexao.cursor()
    for index, linha in df.iterrows():
        cursor.execute(
            "INSERT INTO vendas (produto, categoria, valor, data_venda, regiao) VALUES (%s, %s, %s, %s, %s)",
            (linha["produto"], "Diversos", linha["preco_unitario"], linha["data_pedido"], "Online")
        )
    conexao.commit()
    cursor.close()
    conexao.close()
    print(f"Carregadas {len(df)} linhas no PostgreSQL")

with DAG(
    "pipeline_datashop",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    extrair_task = PythonOperator(
        task_id="extrair_csv",
        python_callable=extrair
    )

    transformar_task = PythonOperator(
        task_id="limpar_dados",
        python_callable=transformar
    )

    carregar_task = PythonOperator(
        task_id="carregar_banco",
        python_callable=carregar
    )

    extrair_task >> transformar_task >> carregar_task
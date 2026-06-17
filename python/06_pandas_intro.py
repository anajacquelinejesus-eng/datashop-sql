import pandas as pd

df = pd.read_csv("python/pedidos_novos.csv")

print("--- Primeiras linhas ---")
print(df.head())          # mostra as primeiras 5 linhas (útil pra tabelas grandes)

print("\n--- Informações gerais ---")
print(df.info())          # mostra tipos de dados e se tem valores nulos

print("\n--- Nomes das colunas ---")
print(df.columns)         # lista só os nomes das colunas

print("\n--- Quantidade de linhas e colunas ---")
print(df.shape)           # (linhas, colunas)
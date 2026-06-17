import pandas as pd

df = pd.read_csv("python/pedidos_novos.csv")

print("--- Dados originais ---")
print(df)
print("Total de linhas:", len(df))


# PROBLEMA 1: espaços extras no email
# .str.strip() remove espaços do início e do fim de cada texto
df["email"] = df["email"].str.strip()


# PROBLEMA 2: linhas duplicadas
# .drop_duplicates() remove linhas que são EXATAMENTE iguais
df = df.drop_duplicates()


# PROBLEMA 3: valor nulo na quantidade
# .fillna() preenche valores nulos com algo - aqui vamos usar 1
# (decisão de negócio: se não informou quantidade, assume que foi 1 unidade)
df["quantidade"] = df["quantidade"].fillna(1)


print("\n--- Dados depois da limpeza ---")
print(df)
print("Total de linhas:", len(df))

print("\n--- Conferindo a coluna quantidade ---")
print(df[["nome_cliente", "quantidade"]])
# Cada dicionário é UMA LINHA, e a lista junta TODAS AS LINHAS
# Isso é literalmente como o Python representa uma tabela do banco de dados

clientes = [
    {"nome": "Ana Silva",    "cidade": "São Paulo",    "idade": 28},
    {"nome": "Bruno Costa",  "cidade": "Curitiba",     "idade": 35},
    {"nome": "Carla Souza",  "cidade": "Recife",       "idade": 22}
]

# Percorrendo cada cliente da lista com um "for" (loop)
for cliente in clientes:
    print(cliente["nome"], "-", cliente["cidade"])
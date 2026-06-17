# LISTA — guarda vários valores em sequência
# Pense como uma fileira de caixinhas numeradas, começando do 0

produtos = ["Notebook Dell", "Mouse Logitech", "Monitor LG"]

print(produtos)          # mostra a lista inteira
print(produtos[0])       # mostra o PRIMEIRO item (índice 0)
print(produtos[1])       # mostra o SEGUNDO item (índice 1)
print(len(produtos))     # len() conta quantos itens tem na lista


# DICIONÁRIO — guarda dados em pares "chave: valor"
# Pense como uma ficha de cadastro, onde cada informação tem um rótulo

cliente = {
    "nome": "Ana Silva",
    "cidade": "São Paulo",
    "idade": 28
}

print(cliente)            # mostra o dicionário inteiro
print(cliente["nome"])    # mostra só o valor da chave "nome"
print(cliente["cidade"])  # mostra só o valor da chave "cidade"
# csv é uma biblioteca que já vem com o Python - não precisa instalar nada
import csv

# "open" abre o arquivo, "r" significa "read" (modo leitura)
# encoding="utf-8" garante que acentos e caracteres especiais sejam lidos corretamente
with open("python/pedidos_novos.csv", mode="r", encoding="utf-8") as arquivo:
    
    leitor = csv.DictReader(arquivo)  # lê cada linha como um dicionário
    
    for linha in leitor:
        print(linha)
import json

with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

for registro in dados:
    nome = registro["Nome"]
    cidade = registro["Cidade"]
    print(f'Nome: {nome} - Cidade: {cidade}')
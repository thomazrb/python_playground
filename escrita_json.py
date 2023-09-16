import json

dados = [
    {"Nome": "Thomaz Rodrigues Botelho","Idade": 10,"Cidade": "São Mateus","Sexo": "Masculino"},
    {
        "Nome": "Zezinho😊",
        "Idade": 15,
        "Cidade": "Vitória",
        "Sexo": "Masculino"
    },
    {
        "Nome": "Mariazinha",
        "Idade": 20,
        "Cidade": "São José dos Campos",
        "Sexo": "Feminino"
    },
    {
        "Nome": "Luizinho",
        "Idade": 10,
        "Cidade": "São Mateus",
        "Sexo": "Masculino"
    },
    {
        "Nome": "Jorginho",
        "Idade": 20,
        "Cidade": "São José dos Campos",
        "Sexo": "Feminino"
    }
]

with open('dados_novo.json', mode='w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii=False)


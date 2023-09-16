import csv

dados = [
    ['Nome','Idade','Cidade','Sexo'],
    ['Thomaz Rodrigues Botelho',10,'São Mateus','Masculino'],
    ['Zezinho',15,'Vitória','Masculino']
    ]

with open('dados_novos.csv', mode='w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo)

    for linha in dados:
        escritor_csv.writerow(linha)
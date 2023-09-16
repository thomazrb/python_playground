import csv

with open('dados.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)

    #Pula o cabeçalho    
    next(leitor_csv)

    for linha in leitor_csv:
        nome, idade, cidade, sexo = linha
        if cidade == 'São Mateus':
            print(f'Nome: {nome} - Idade: {idade} - Cidade: {linha[2]}')


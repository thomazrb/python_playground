import csv

with open('dados.csv', 'r', encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    dados = list(leitor_csv)
# dados = [
#         ['Nome', 'Idade', 'Cidade', 'Sexo'], 
#         ['Thomaz Rodrigues Botelho', '10', 'São Mateus', 'Masculino'], 
#         ['Zezinho', '15', 'Vitória', 'Masculino'], 
#         ['Mariazinha', '20', 'São José dos Campos', 'Feminino'], 
#         ['Luizinho', '15', 'São Mateus', 'Masculino'], 
#         ['Jorginho', '20', 'São José dos Campos', 'Feminino']
#     ]

for n, linha in enumerate(dados):
    if linha[0] == 'Luizinho':
        dados[n][1] = 10
input()
with open('dados.csv', mode='w', encoding='utf-8', newline='') as arquivo:
    escritor_csv = csv.writer(arquivo)

    for linha in dados:
        escritor_csv.writerow(linha)
try:
    arquivo = open('teste.txt', mode='r', encoding='utf-8')
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print('O arquivo não foi encontrado!')
else:
    arquivo.close()

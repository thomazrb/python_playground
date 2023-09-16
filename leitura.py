arquivo = open('teste.txt', mode='r', encoding='utf-8')
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

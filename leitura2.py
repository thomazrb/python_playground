with open('teste.txt', mode='r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        print(f'Linha: {linha.strip()}')

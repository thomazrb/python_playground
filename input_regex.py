import re

def validar_idade(idade):
    # Expressão regular para validar um número inteiro positivo
    padrao = r'^[1-9][0-9]*$'
    return re.match(padrao, idade)

while True:
    idade = input("Digite sua idade (apenas números inteiros positivos): ")
    
    if validar_idade(idade):
        idade = int(idade)
        print(f"Sua idade é: {idade}")
        break
    else:
        print("Idade inválida. Tente novamente.")
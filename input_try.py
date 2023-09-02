while True:
    try:
        idade = int(input("Digite sua idade (apenas números inteiros positivos): "))    
        if idade > 0:
            print(f"Sua idade é: {idade}")
            break
        else:
            print("Idade inválida. A idade deve ser um número inteiro positivo.")
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números inteiros positivos.")
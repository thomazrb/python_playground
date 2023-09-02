try:
    # Código que pode gerar um erro
    x = 10 / 0  # Isso gera uma exceção de divisão por zero
except ZeroDivisionError:
    # Lidar com o erro de divisão por zero
    print("Erro: Divisão por zero.")
else:
    # Código a ser executado se nenhum erro ocorrer
    print("A divisão foi bem-sucedida. O resultado é:", x)
finally:
    # Código a ser sempre executado, com ou sem erro
    print("Finalizando o programa...")

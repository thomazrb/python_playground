import re

email = input("Digite seu email: ")

if not re.match(r"[^@]+@[^@]+\.[^@]+$", email):
    print("Por favor, insira um endereço de email válido.")

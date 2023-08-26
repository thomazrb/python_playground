print("Hello World!")

nome = "Zezinho"
idade = 10
print("Nome:", nome, "Idade:", idade)
x = "Nome:", nome, "Idade:", idade
print(type(x))

print('Nome: {0} Idade: {1}'.format(nome, idade))
y = 'Nome: {0} Idade: {1}'.format(nome, idade)
print(type(y))

print(f'Nome: {nome} Idade: {idade}')


print('Ola', end=' ')
print('Mundo')

valor = 123.234215
print('valor = {0:.2f}'.format(valor))


print(f'\033[92m Oi\033[0m')

x = """Oi

Teste
!"""

print(x)
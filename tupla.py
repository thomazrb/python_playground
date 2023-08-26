minha_tupla = ("maçã", "banana", "laranja")

print(type(minha_tupla))
print(minha_tupla)

print(minha_tupla[1])
# minha_tupla[1] = 'abacate' <= ERRO!

minha_lista = list(minha_tupla)
print(minha_lista)
minha_lista.sort()
minha_tupla = tuple(minha_lista)
print(minha_tupla)

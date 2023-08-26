minha_lista = [1, 2, 3, 4, 5, "banana", "maçã"]

for item in minha_lista:
    print(item)


for numero in range(0, 10, 2 ):
    print(numero)


for indice, item in enumerate(minha_lista):
    print("Indice: {0} - Elemento: {1}".format(indice, item))


# evitar fazer assim:
indice = 0
for item in minha_lista:
    print("Indice: {0} - Elemento: {1}".format(indice, item))
    indice = indice + 1
    
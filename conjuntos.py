# lista = []
# tuplas = ()
# dicionários = {} conjunto chave-valor
# conjuntos = {}

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
print(conjunto1)
print(conjunto2)

uniao = conjunto1 | conjunto2
print(uniao)

intersecao = conjunto1 & conjunto2
print(intersecao)

diferenca = conjunto1 - conjunto2
print(diferenca)

lista_de_compras = ["banana", "maçã", "goiaba", "abacate", "morango"]
carrinho = ["maçã", "morango", "abacate"]

set_lista_de_compras = set(lista_de_compras)
set_carrinho = set(carrinho)

print(set_lista_de_compras)
print(set_carrinho)

set_falta = set_lista_de_compras - set_carrinho
print(set_falta)

falta = list(set_falta)
print(falta)

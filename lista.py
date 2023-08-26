minha_lista = ["maçã", "banana", "laranja"]

print(type(minha_lista))
print(minha_lista)

minha_lista.append("morango")
print(minha_lista)

minha_lista.insert(2, "maracujá")
print(minha_lista)

minha_lista.remove("laranja")
print(minha_lista)

fruta = minha_lista.pop(2)
print(minha_lista)
print(fruta)

minha_lista.sort(reverse=True)

print(minha_lista)


with open('foto.jpg', 'rb') as foto:
    bits = foto.read()

with open('nova_foto.jpg', 'wb') as nova_foto:
    nova_foto.write(bits)
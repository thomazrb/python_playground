while True:
    try:
        peso = float(input('Digite o Peso: '))
        break
    except ValueError:
        print('Valor Inválido. Digite novamente')

while True:
    try:
        altura = float(input('Digite a altura: '))
        break
    except ValueError:
        print('Valor Inválido. Digite novamente')

try:
    imc = peso / (altura * altura)
except ZeroDivisionError:
    print('Erro processando o IMC. A altura está zerada')
else:
    print('O imc é: ', imc)
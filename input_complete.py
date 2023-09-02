import re

def validar_data(data):
    # Expressão regular para validar uma data no formato "dd/mm/aaaa"
    padrao = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
    return re.match(padrao, data)

while True:
    data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    
    if validar_data(data):
        try:
            # Separar o dia, mês e ano
            dia, mes, ano = map(int, data.split('/'))
            
            # Validar a data (apenas um exemplo simples)
            if 1900 <= ano <= 2100:
                print(data.split('/'))
                print(f"Sua data de nascimento é: {data}")
                print("Dia", dia)
                print("Mês", mes)
                print("Ano", ano)
                break
            else:
                print("Data de nascimento fora do intervalo permitido.")
        except ValueError:
            print("Erro ao processar a data. Tente novamente.")
    else:
        print("Data de nascimento inválida. Tente novamente.")
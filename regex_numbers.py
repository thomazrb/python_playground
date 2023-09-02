import re

padrao = r'^[0-9]+$'

# Exemplos de strings para testar
strings_para_testar = ["12345", "0", "9876543210", "abc123", "12 34"]

for string in strings_para_testar:
    if re.match(padrao, string):
        print(f'A string "{string}" é um número válido.')
    else:
        print(f'A string "{string}" não é um número válido.')

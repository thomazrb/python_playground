nota = float(input('Digite a nota do aluno: '))

print(nota)

# uma única estrutura...
if nota >= 9.0:
    conceito = 'A'
elif nota >= 7.0:
    conceito = 'B'
elif nota >= 5.0:
    conceito = 'C' 
else:
    conceito = 'D'

print(f'Conceito: {conceito}')

print('---')

nota = float(input('Digite a nota do aluno: '))

print(nota)

# 4 estruturas independentes... neste caso não vai funcionar.
if nota >= 9.0:
    conceito = 'A'
if nota >= 7.0:
    conceito = 'B'
if nota >= 5.0:
    conceito = 'C' 
if nota < 5.0:
    conceito = 'D'

print(f'Conceito: {conceito}')
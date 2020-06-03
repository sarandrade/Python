# Percorrendo string
palavra = 'PARALELO'
for letra in palavra:
    print(letra, end=', ')
print('FIM')

# Percorrendo lista
aprovados = ['Sara', 'Túlio', 'Ana', 'Mari']
for aluno in aprovados:
    print(aluno, end=' ')
print()

for posicao, aluno in enumerate(aprovados):
    print(f'{posicao + 1} -> {aluno}')

# Percorrendo tupla
dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é dia {dia}')

# Percorrendo conjunto (set)
for letra in set('Uhum'):
    print(letra, end=' ')
print()

for numero in {7, 2, 6, 9, 15}:
    print(numero, end=' ')

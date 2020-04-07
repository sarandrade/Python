# Desafios 89

lista = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    
    lista.append([nome, [nota1, nota2], media])

    opc = ' '
    while opc not in 'SN':
        opc = input('Quer continuar [S/N]? ').upper().strip()[0]
    
    if opc == 'N':
        break

print('-+-'*10)
print(f'{"N°":<4}{"NOME":<10}  {"MÉDIA":>8}')
print('--'*15)

for posicao, aluno in enumerate(lista): 
    print(f'{posicao + 1:<4}{aluno[0]:<10}{aluno[2]:>8}')
print('--'*15)

num = 0
while num != 99:
    num = int(input('Mostras a nota de qual aluno (99 fim)? '))
    if num <= len(lista):
        print(f'Notas de {lista[num - 1][0]}: {lista[num - 1][1]}')
        print('--'*15)
    elif num != 99: 
        print('Opção Inválida!')

print('\nFinalizando...')
print('<<< VOLTE SEMPRE >>>')

'''
=> Primeira tentativa

boletim = []
alunos = []
notas = []

while True:
    alunos.append(input('Nome: ').strip())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    alunos.append(notas[:])
    boletim.append(alunos[:])
    alunos.clear()
    notas.clear()

    opc = ' '
    while opc not in 'SN':
        opc = input('Quer continuar [S/N]? ').upper().strip()[0]
    
    if opc == 'N':
        break

print('-+-'*10)
print('N° NOME             MÉDIA')
print('--'*15)

for posicao, aluno in enumerate(boletim): 
    for pos, termo in enumerate(aluno):
        if pos % 2 == 0:
            print(f'{posicao + 1}  {termo:<10}', end='')
        else:
            media = (termo[0] + termo[1]) / 2
            print(f'        {media}')
print('--'*15)

num = 0
while num != 99:
    num = int(input('Mostras a nota de qual aluno (99 fim)? '))
    if num <= len(boletim):
        print(f'Notas de {boletim[num - 1][0]}: {boletim[num - 1][1]}')
        print('--'*15)
    elif num != 99: 
        print('Opção Inválida!')

print('\nFinalizando...')
print('<<< VOLTE SEMPRE >>>')
'''
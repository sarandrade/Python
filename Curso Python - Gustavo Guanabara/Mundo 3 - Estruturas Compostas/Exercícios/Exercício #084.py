# Desafios 84

grupo = []
pessoa = []
maior = menor = 0

while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))

    if len(grupo) == 0:
        maior = menor = pessoa[1] 
    if pessoa[1] > maior:
        maior = pessoa[1] 
    if pessoa[1] < menor:
        menor = pessoa[1]

    grupo.append(pessoa[:])
    pessoa.clear()

    opc = ' '
    while opc not in 'SN':
        opc = input('Quer continuar [S/N]? ').upper().strip()[0]
    
    if opc == 'N':
        break

print('-+-'*10)
print(f'Total de pessoas: {len(grupo)}')

print(f'Maior peso: {maior}Kg =>', end=' ')
for i in grupo:
    if i[1] == maior:
        print(i[0], end=' ')

print(f'\nMenor peso: {menor}Kg =>', end=' ')
for i in grupo:
    if i[1] == menor:
        print(i[0], end=' ')
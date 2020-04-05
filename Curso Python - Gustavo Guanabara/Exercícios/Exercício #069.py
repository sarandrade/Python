# Desafios 69

numhomem = mulher20 = mais18 = 0

while True:
    print('-=-'*10)
    print('  CADASTRE UMA PESSOA  ')
    print('-=-'*10)

    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo [F/M]: ').upper().strip()[0]
    print('-=-'*10)

    if sexo == 'M':
        numhomem += 1 

    if sexo == 'F' and idade < 20:
        mulher20 += 1 

    if idade > 18:
        mais18 += 1

    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Quer continuar [S/N]? ').upper().strip()[0]

    if opcao == 'N':
        break

print('\n==== FIM DO PROGRAMA ====')
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Total de homens cadastrados: {numhomem}')
print(f'Total de mulheres com menos de 20 anos: {mulher20}')

'''
=> Outra forma 

numhomem = mulher20 = mais18 = 0

while True:
    print('-=-'*10)
    print('  CADASTRE UMA PESSOA  ')
    print('-=-'*10)

    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').upper().strip()[0]
    print('-=-'*10)

    if sexo == 'M':
        numhomem += 1 
    elif sexo == 'F' and idade < 20:
        mulher20 += 1 
    else:
        print('Opção Inválida!! Tente de novo...')
        sexo = input('Sexo [F/M]: ').upper().strip()[0]
        print('-=-'*10)

    if idade > 18:
        mais18 += 1

    opcao = input('Quer continuar [S/N]? ').upper().strip()[0]

    if opcao == 'N':
        break
    elif opcao != 'S':
        print('Opção Inválida!! Tente de novo...')
        opcao = input('Quer continuar [S/N]? ').upper().strip()[0]

print('\n==== FIM DO PROGRAMA ====')
print(f'Total de pessoas com mais de 18 anos: {mais18}')
print(f'Total de homens cadastrados: {numhomem}')
print(f'Total de mulheres com menos de 20 anos: {mulher20}')
'''
# Desafios 79

lista = []

while True:
    num = int(input('Digite um número: '))

    if num in lista:
        print('Valor duplicado... \nNão vou adicionar...')
    else:
        lista.append(num)
        print('Valor adicionado!!')


    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Quer continuar [S/N]? ').upper().strip()[0]
    
    if opcao == 'N':
        break

print('-+-'*20)
print(f'Você digitou os valores: {sorted(lista)}')
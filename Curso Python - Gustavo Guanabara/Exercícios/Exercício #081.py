# Desafios 81

lista = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)

    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Deseja continuar [S/N]? ').upper().strip()[0]
    
    if opcao == 'N':
        break

print('-+-'*20)

print(f'{len(lista)} valores foram digitados.')

lista.sort(reverse=True)
print(f'Em ordem decrescente: {lista}')

if 5 in lista:
    print('O valor 5 se encontra na posição:', end=' ')
    for posicao, termo in enumerate(lista):
        if termo == 5:
            print(f'{posicao}', end=' ')
else:
    print('O valor 5 não está na lista.')
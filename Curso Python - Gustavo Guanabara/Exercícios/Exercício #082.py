# Desafios 82

lista = []
par = []
impar = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)

    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Deseja continuar [S/N]? ').upper().strip()[0]
    
    if opcao == 'N':
        break

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print('-+-'*20)
print(f'Lista completa: {lista}')
print(f'Lista par: {par}')
print(f'Lista ímpar: {impar}')
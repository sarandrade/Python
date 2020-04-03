# Desafios 50

soma = 0

for i in range(0, 6):
    num = float(input('Digite um número: '))

    if num % 2 == 0:
        soma += num

print('A soma dos números pares digitados é igual a {}.'.format(soma))
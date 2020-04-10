# Desafios 52

from math import trunc

num = int(input('Digite um número inteiro: '))

limite = trunc(num ** (1/2))

soma = 0

for i in range(2, limite + 1):

    if num % i == 0:
        print('{} é divisível por {}.'.format(num, i))
        soma += i

if soma == 0:
    print('O número é divisível apenas por 1 e por ele mesmo.')
    print('Logo, {} é um número primo!!'.format(num))
else:
    print('{} não é um número primo.'.format(num))
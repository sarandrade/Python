# Desafios 60


num = int(input('Digite um número: '))
fatorial = 1
salvo = num

print('Calculando {}! = '.format(salvo), end='')

while num != 0:
    
    print('{}'.format(num), end='')
    print(' x ' if num > 1 else ' = ', end='')
    fatorial *= num
    num -= 1

print('{}'.format(fatorial))

'''
=> Utilizando a estrutura for:

num = int(input('Digite um número: '))
fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

print('=> {}! = {}'.format(num, fatorial))

=> Utilizando a função factorial

from math import factorial

num = int(input('Digite um número: '))

fatorial = factorial(num)

print('=> {}! = {}'.format(num, fatorial))
''' 
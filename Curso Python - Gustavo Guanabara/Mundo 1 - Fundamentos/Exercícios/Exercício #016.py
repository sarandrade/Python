# Desafios 16

from math import trunc

num = float(input('Digite um número real: '))

print('A parte inteira do número {} é {}.'.format(num, trunc(num)))

'''
Utilizando uma função interna

num = float(input('Digite um número real: '))

print('A parte inteira do número {} é {}.'.format(num, int(num)))
'''
# Aula #08 - Utilizando Módulos

'''
- import modulo 
- from módulo import função_1, função_2
'''

import math

num = float(input('Digite um número: '))

raiz = math.sqrt(num) # Raiz quadrada

print('A raiz do número {} é {}.'.format(num, math.ceil(raiz))) # Arredonda para cima
print('A raiz do número {} é {}.'.format(num, math.floor(raiz))) # Arredonda para baixo

'''
ou 

from math import sqrt, ceil, floor

num = float(input('Digite um número: '))

raiz = sqrt(num) # Raiz quadrada

print('A raiz do número {} é {}.'.format(num, ceil(raiz))) # Arredonda para cima
print('A raiz do número {} é {}.'.format(num, floor(raiz))) # Arredonda para baixo
''' 

import random

num1 = random.random()
num2 = random.randint(1, 10)

print(num1)
print(num2)

import emoji

print(emoji.emojize('Olá, Mundo :sunglasses:', use_aliases=True))
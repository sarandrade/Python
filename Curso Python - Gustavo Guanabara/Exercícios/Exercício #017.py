# Desafios 17

from math import hypot

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

print('A hipotenusa é {:.2f}'.format(hypot(co, ca)))
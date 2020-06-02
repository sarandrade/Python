# import math -> math.pi
# from math import pi -> pi
# import math as mt -> mt.pi
from math import pi


def circulo(raio):
    return pi * raio ** 2


# Variáveis
raio = float(input('\nInforme o raio: '))
area = circulo(raio)

print(f'A área da circunferência é {area} metros.\n')

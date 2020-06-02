# import math -> math.pi
# from math import pi -> pi
# import math as mt -> mt.pi
from math import pi
import sys


def circulo(raio):
    return pi * float(raio) ** 2


# Variáveis
raio = sys.argv[1]
area = circulo(raio)

print(f'A área da circunferência é {area} metros.\n')

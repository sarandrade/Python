# import math -> math.pi
# from math import pi -> pi
# import math as mt -> mt.pi
from math import pi
import sys
import errno


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print('É necessário informar o raio do círculo')
    print('Sintaxe: python {} <raio>'.format(sys.argv[0]))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        # sys.exit(1) ou 
        sys.exit(errno.EPERM)

    # Variáveis
    raio = sys.argv[1]
    area = circulo(raio)

    print(f'\nA área da circunferência é {area} metros.\n')

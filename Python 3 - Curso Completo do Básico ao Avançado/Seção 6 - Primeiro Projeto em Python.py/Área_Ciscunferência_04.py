# import math -> math.pi
# from math import pi -> pi
# import math as mt -> mt.pi
from math import pi
import sys
import errno


class TerminalColor:
    erro = '\033[91m'
    normal = '\033[0m'


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print('\nÉ necessário informar o raio do círculo')
    print('Sintaxe: python {} <raio>'.format(sys.argv[0]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        print()
        # sys.exit(1) ou 
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.erro + 'O raio deve ser um valor númerico.\n' + 
              TerminalColor.normal)
        sys.exit(errno.EINVAL)

    # Variáveis
    raio = sys.argv[1]
    area = circulo(raio)
    print(f'\nA área da circunferência é {area} metros.\n')

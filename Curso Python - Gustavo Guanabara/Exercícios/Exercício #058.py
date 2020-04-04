# Desafios 58

from time import sleep
from random import randint

para = 0

while not (para == 1):
    jogador = int(input('Digite um número entre 0 e 10: '))

    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print(' COMPUTADOR ESCOLHENDO ', end='')
    print('.', end='')
    sleep(1)
    print('.', end='')
    sleep(1)
    print('.')
    sleep(1)

    comp = randint(0, 10)

    if jogador == comp:
        print('Jogador X Computador')
        print('[ {} ] X [ {} ] -> Acertou!!'.format(jogador, comp))
        print('...Você ganhou...')
        para =1
    else:
        print('Jogador X Computador')
        print('[ {} ] X [ {} ] -> Errou!!'.format(jogador, comp))
        print('Tente novamente...')


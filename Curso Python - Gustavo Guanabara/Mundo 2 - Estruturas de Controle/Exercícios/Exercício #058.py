# Desafios 58

# 1 - Cada rodada um número é sorteado 

from time import sleep
from random import randint

print('-+-'*10)
print('JOGO DE ADIVINHAR')
print('-+-'*10)

vitoria = False

while not vitoria:
    jogador = int(input('\nDigite um número entre 0 e 10: '))

    print('... COMPUTADOR ESCOLHENDO ...')
    sleep(1)
    print('-+-'*10)

    comp = randint(0, 10)

    if jogador == comp:
        print('Jogador X Computador')
        print('[ {} ] X [ {} ] -> Acertou!!'.format(jogador, comp))
        print('...Você ganhou...')
        print('-+-'*10)
        vitoria = True
    else:
        print('Jogador X Computador')
        print('[ {} ] X [ {} ] -> Errou!!'.format(jogador, comp))
        print('Tente novamente...')
        print('-+-'*10)

'''
# 2 - Um único número é sorteado para todo o jogo 

from time import sleep
from random import randint

print('-+-'*10)
print('JOGO DE ADIVINHAR')
print('-+-'*10)

vitoria = False
palpites = 0

print('... COMPUTADOR ESCOLHENDO ...')
sleep(1)
print('-+-'*10)
comp = randint(0, 10)

while not vitoria:
    jogador = int(input('Digite um número entre 0 e 10: '))
    palpites += 1

    if jogador == comp:
        print('...Você ganhou...')
        print('-+-'*10)
        vitoria = True
    else:
        print('Tente novamente...')

        if  jogador > comp:
            print('O número é menor...')
            print('-+-'*10)
        elif jogador < comp:
            print('O número é maior...')
            print('-+-'*10)

print(f'Acertou com {palpites} tentativas.')
'''
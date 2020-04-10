# Desafios 91

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador_1': randint(1, 6), 
        'Jogador_2': randint(1, 6), 
        'Jogador_3': randint(1, 6), 
        'Jogador_4': randint(1, 6)}

print('-+-'*7)
print('== JOGO DE DADOS ==')
print('-+-'*7)
print('Valores sorteados:')

for k, v in jogo.items():
    print(f'O {k} tirou: {v}')
    sleep(1)

print('-+-'*7)
print('    == RANKING ==')
print('-+-'*7)

ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for pos, dic in enumerate(ranking):
    print(f'{pos + 1}° lugar: {dic[0]} => {dic[1]}')
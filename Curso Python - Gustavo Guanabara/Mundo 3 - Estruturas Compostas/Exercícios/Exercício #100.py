# Desafios 100

from random import randint
from time import sleep

def somapar(lst):
    soma = 0
    for n in range(0, len(lst)):
        if lst[n] % 2 == 0:
            soma += lst[n]
    print('-=-'*10)
    print(f'Somando os pares de: {lst}')
    sleep(1)
    print(f'Soma = {soma}')
    print('-=-'*10)

def sorteio(lst):
    for n in range(0, 5):
        lst.append(randint(0, 10))
    print('-=-'*10)
    print('Sorteando 5 valores para a lista...')
    sleep(1)
    print(lista)
    print('Pronto!')


lista = list()
sorteio(lista)
somapar(lista)
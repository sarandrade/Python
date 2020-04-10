# Desafios 19

from random import randint

lista = input('Digite o nome dos 4 alunos: ').split()

escolhido = randint(0,3)

print('O sorteado foi {}'.format(lista[escolhido]))
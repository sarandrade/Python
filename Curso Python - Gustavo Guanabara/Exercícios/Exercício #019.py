# Desafios 19

import random

lista = input('Digite o nome dos 4 alunos: ').split()

escolhido = random.randint(0,3)

print('O sorteado foi {}'.format(lista[escolhido]))
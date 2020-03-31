# Desafios 20

import random 

lista = input('Digite o nome dos 4 alunos: ').split()

'''
escolhido = randint(0,3)

print('O primeiro sorteado foi {}.'.format(lista[escolhido]))
lista.pop(escolhido)
escolhido = randint(0,2)

print('O segundo sorteado foi {}.'.format(lista[escolhido]))
lista.pop(escolhido)
escolhido = randint(0,1)

print('O terceiro sorteado foi {}.'.format(lista[escolhido]))
lista.pop(escolhido)

print('Sobrando então {}.'.format(lista[0]))
'''

random.shuffle(lista)

print('-'*20)
print('Ordem dos sorteados \n{:^17} \n{:^17} \n{:^17} \n{:^17}'.format(lista[0], lista[1], lista[2], lista[3]))
print('-'*20)
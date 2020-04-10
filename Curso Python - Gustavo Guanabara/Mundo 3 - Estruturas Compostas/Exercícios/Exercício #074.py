# Desafios 74

from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print('Os valores sorteados foram:', end=" ")
for i in tupla:
    print(i, end=' ')

print(f'\nO maior valor sorteado foi: {max(tupla)}')
print(f'O menor valor sorteado foi: {min(tupla)}')

'''
=> Ou 

a = randint(0, 10)
b = randint(0, 10)
c = randint(0, 10)
d = randint(0, 10)
e = randint(0, 10)

tupla = (a, b, c, d, e)

print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi: {sorted(tupla)[4]}')
print(f'O menor valor sorteado foi: {sorted(tupla)[0]}')
'''
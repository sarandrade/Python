# Desafios 74

from random import randint

a = randint(0, 10)
b = randint(0, 10)
c = randint(0, 10)
d = randint(0, 10)
e = randint(0, 10)

tupla = (a, b, c, d, e)

print(f'Os valores sorteados foram: {tupla}')
print(f'O maior valor sorteado foi: {sorted(tupla)[4]}')
print(f'O menor valor sorteado foi: {sorted(tupla)[0]}')
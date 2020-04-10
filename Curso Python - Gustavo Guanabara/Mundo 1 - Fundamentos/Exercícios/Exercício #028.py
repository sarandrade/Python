# Desafios 28

from random import randint
from time import sleep

num = int(input('Qual número foi o escolhido pelo computador? '))

esc = randint(0,5)

print('-=-'*20)
print('PROCESSANDO...')
print('-=-'*20)
sleep(2)

print('Acertou!!' if num == esc else 'Errou kkk. O número certo era {}.'.format(esc))
# Desafios 88

from random import randint

print('-+-'*12)
print('         JOGA NA MEGA SENHA')
print('-+-'*12)

num = int(input('Quantos jogos você quer sortear? '))

print(f'\n-=-=- SORTEANDO {num} JOGOS -=-=-')

jogo = []

for j in range(0, num):

    for n in range(0, 6):
        while True:
            sort = randint(0, 60)
            if sort not in jogo:
                break

        jogo.append(sort)

    print(f'Jogo {j + 1:>2} => {sorted(jogo)}')
    jogo.clear()

print('-+-'*12)
print('            BOA SORTE!!')
print('-+-'*12)
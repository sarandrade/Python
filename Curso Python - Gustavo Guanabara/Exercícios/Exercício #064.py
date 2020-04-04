# Desafios 64

num = 0
soma = 0
i = 0

while num != 999:
    num = int(input('Digite um número inteiro: '))

    if num != 999:
        soma += num
        i += 1

print('A soma dos {} números digitados é {}.'.format(i, soma))
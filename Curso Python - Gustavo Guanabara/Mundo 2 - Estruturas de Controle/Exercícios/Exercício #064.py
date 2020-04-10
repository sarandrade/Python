# Desafios 64

num = i = soma = 0

num = int(input('Digite um número inteiro: '))

while num != 999:
    soma += num
    i += 1
    num = int(input('Digite um número inteiro: '))
    

print('A soma dos {} números digitados é {}.'.format(i, soma))

'''
while num != 999:
    num = int(input('Digite um número inteiro: '))

    if num != 999:
        soma += num
        i += 1

print('A soma dos {} números digitados é {}.'.format(i, soma))
'''
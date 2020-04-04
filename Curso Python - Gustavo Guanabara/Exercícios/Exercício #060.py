# Desafios 60


num = int(input('Digite um número: '))
fatorial = 1
salvo = num

while num != 0:
    fatorial *= num
    num = num - 1 

print('=> {}! = {}'.format(salvo, fatorial))

'''
=> Utilizando a estrutura for:

num = int(input('Digite um número: '))
fatorial = 1

for i in range(1, num + 1):
    fatorial *= i

print('=> {}! = {}'.format(num, fatorial))
''' 
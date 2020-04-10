# Desafios 75

a = int(input('Digite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))
d = int(input('Digite um valor: '))

tupla = (a, b, c, d)

'''
=> Ou 
tupla = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')))
'''

# A
print(f'Quantas vezes apareceu o valor 9? {tupla.count(9)}')

# B 
if 3 in tupla:
    print(f'Em que posição foi digitado o primeiro valor 3? {tupla.index(3) + 1}')
else:
    print('O valor 3 não foi digitado.')

# C 
print('Quais foram os números pares? ', end='')

for num in tupla:
    if num % 2 == 0:
        print(num, end=' ')
# Desafios 61

'''
=> Utilizando a estrutura for: 

inicio = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for i in range(inicio, inicio + 10 * razao, razao):
    print(i, end=' ')
'''

inicio = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

i = 10

while i != 0:
    print(inicio, end=' ')
    inicio = inicio + razao
    i -= 1
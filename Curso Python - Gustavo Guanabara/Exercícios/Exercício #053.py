# Desafios 53

from math import trunc

frase = input('Digite a frase: ').strip().upper().split()

frase = ''.join(frase)

tamanho = len(frase)

x = 0

for i in range(0, trunc(tamanho/2) + 1):
    fim = tamanho - i - 1

    if frase[i] != frase[fim]: 
        x += i # A frase não é um palíndromo

if x > 0:
    print('A frase não é um palíndromo.')    
else:
    print('A frase é um palíndromo.')

'''
-- ou --

frase = input('Digite a frase: ').strip().upper().split()

junto = ''.join(frase)

tamanho = len(junto)

inverso = ''

for i in range(tamanho -1, -1, -1):
    inverso += junto[i]

print(inverso)

if junto == inverso:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')  
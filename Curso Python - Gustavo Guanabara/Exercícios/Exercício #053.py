# Desafios 53

from math import trunc

frase = input('Digite a frase: ').strip().upper()

tamanho = len(frase)

x = 0

for i in range(0, trunc(tamanho/2) + 1):
    fim = tamanho - i - 1

    if frase[i] != frase[fim]: 
        x += i # A frase não é um políndromo
    else:
        x = 0

if x > 0:
    print('A frase não é um políndromo.')    
else:
    print('A frase é um políndromo.')
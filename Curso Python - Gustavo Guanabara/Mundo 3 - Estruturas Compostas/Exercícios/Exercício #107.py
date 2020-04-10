# Desafios 107

import moeda

num = float(input('Digite um valor: R$  '))

print(f'A metade de {num} é {moeda.metade(num)}.')
print(f'O dobro de {num} é {moeda.dobro(num)}.')
print(f'Aumentando em 10%, temos {moeda.aumentar(num, 10)}.')
print(f'Reduzindo em 13%, temos {moeda.diminuir(num, 13)}.')
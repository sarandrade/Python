# Desafios 107

import moeda

num = float(input('Digite um valor: R$'))

print(f'A metade de {num} é {moeda.metade(num):.2f}.')
print(f'O dobro de {num} é {moeda.dobro(num):.2f}.')
print(f'Aumentando em 10%, temos {moeda.aumentar(num, 10):.2f}.')
print(f'Reduzindo em 13%, temos {moeda.diminuir(num, 13):.2f}.')
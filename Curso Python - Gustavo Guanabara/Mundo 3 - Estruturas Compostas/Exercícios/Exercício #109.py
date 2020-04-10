# Desafios 109

from moeda import * # Importa tudo de moeda

num = float(input('Digite um valor: R$  '))

print(f'A metade de {moeda(num)} é {metade(num, True)}.')
print(f'O dobro de {moeda(num)} é {dobro(num, True)}.')
print(f'Aumentando em 10%, temos {aumentar(num, 10, True)}.')
print(f'Reduzindo em 13%, temos {diminuir(num, 13, True)}.')
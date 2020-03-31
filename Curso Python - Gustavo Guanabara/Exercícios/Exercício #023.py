# Desafios 23

num = int(input('Digite um número: '))

uni = num // 1 % 10
dez = num //10 % 10
cen = num //100 % 10
mil = num //1000 % 10

print('Milhar  -> {} \nCentena -> {}\nDezena  -> {} \nUnidade -> {}'.format(mil, cen, dez, uni))
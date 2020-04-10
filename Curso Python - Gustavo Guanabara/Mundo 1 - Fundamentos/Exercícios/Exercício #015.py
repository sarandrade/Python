# Desafios 15

km = float(input('Quantos Km rodados? '))
dias = float(input('Quantos dias alugados? '))

total = 60 * dias + 0.15 * km

print('O total a pagar é R${:.2f}'.format(total))
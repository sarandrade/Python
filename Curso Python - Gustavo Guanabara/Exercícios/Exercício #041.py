# Desafios 41

from datetime import date

nasc = int(input('Digite o ano de seu nascimento: '))

hoje = date.today().year

idade = hoje - nasc

print('Você tem {:.0f} anos.'.format(idade))

if idade <= 9:
    categ = 'Mirin'
elif idade <= 14:
    categ = 'Infantil'
elif idade <= 19:
    categ = 'Junior'
elif idade <= 25: 
    categ = 'Sênior'
else:
    categ = 'Master'

print('Logo, sua categoria é -> {}.'.format(categ))
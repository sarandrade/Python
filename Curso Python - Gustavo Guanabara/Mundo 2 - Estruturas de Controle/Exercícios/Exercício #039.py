# Desafios 39

from datetime import date

ano = int(input('Digite o ano em que nasceu: '))

hoje = date.today().year

idade = hoje - ano

print('Você nasceu em {} e fez/faz {} anos em {}.'.format(ano, idade, hoje))

if idade > 18:
    atras = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(atras))
elif idade < 18:
    adian = 18 - idade
    print('Você deverá se alistar em {} anos.'.format(adian))
else:
    print('Atenção!! Você deve se alistar esse ano.')
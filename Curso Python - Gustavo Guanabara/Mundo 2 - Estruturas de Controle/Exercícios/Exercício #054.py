# Desafios 54

from datetime import date

maiores = 0
menores = 0
hoje = date.today().year

for i in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))

    idade = hoje - ano

    if idade >= 21:
        maiores += 1
    else:
        menores += 1

print('{} pessoas atingiram a maioridade.'.format(maiores))
print('{} pessoas ainda não atingiram a maioridade.'.format(menores))
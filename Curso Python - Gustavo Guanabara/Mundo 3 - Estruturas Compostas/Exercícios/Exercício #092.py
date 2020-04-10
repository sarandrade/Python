# Desafios 92

from datetime import date

dic = {}

dic['Nome'] = input('Nome: ')

nasc = int(input('Ano de nascimento: '))
hoje = date.today().year
idade = hoje - nasc
dic['Idade'] = idade

dic['CTPS'] = int(input('Carteira de Trabalho (0 não se não tiver): '))

if dic['CTPS'] != 0:
    cont = int(input('Ano de contratação: '))
    dic['contratacao'] = cont
    dic['Aposentadoria'] = idade - (hoje - cont) + 35
    dic['Salário'] = float(input('Salário: R$'))

print('-+-'*10)
for k, v in dic.items():
    print(f'{k} => {v}')
print('-+-'*10)
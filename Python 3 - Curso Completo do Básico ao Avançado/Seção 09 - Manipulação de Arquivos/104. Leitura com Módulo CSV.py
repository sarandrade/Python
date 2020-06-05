import csv

with open('Pessoas.csv', encoding='utf8') as arquivo:
    for pessoa in csv.reader(arquivo):
        print('Nome: {} | Idade: {}'.format(*pessoa))

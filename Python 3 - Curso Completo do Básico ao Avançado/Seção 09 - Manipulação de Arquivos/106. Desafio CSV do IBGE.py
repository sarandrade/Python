# ISO-8859-1
import csv
# from urllib import request -> Abre um url

with open('desafio_ibge.csv', encoding='ISO-8859-1') as arquivo:
    for linha in csv.reader(arquivo):
        print('{} | {}'.format(linha[8], linha[3]))

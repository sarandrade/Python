# ISO-8859-1
import csv
from urllib import request # -> Abre um url


def read(url):
    with request.urlopen(url) as arquivo:
        print('Baixando o CSV...')
        dados = arquivo.read().decode('latin1')
        print('Download completo!')
        for linha in csv.reader(dados.splitlines()):
            print('{} | {}'.format(linha[8], linha[3]))


if __name__ == "__main__":
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')

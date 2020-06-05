arquivo = open('Pessoas.csv', encoding='utf8')
# Lê o arquivo sob demanda, não carrega tudo na memória -> Stream

for pessoa in arquivo:
    # strip() -> Tira os espaços em branco no começo e no fim da string
    # split(',') -> Quebra a string em ','
    print('Nome: {} | Idade: {}'.format(*pessoa.strip().split(',')))

arquivo.close()

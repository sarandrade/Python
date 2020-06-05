# O with fecha o arquivo quando o bloco é finalizado
with open('Pessoas.csv', encoding='utf8') as arquivo:
    for pessoa in arquivo:
        # strip() -> Tira os espaços em branco no começo e no fim da string
        # split(',') -> Quebra a string em ','
        print('Nome: {} | Idade: {}'.format(*pessoa.strip().split(',')))

if arquivo.closed:
    print('Arquivo foi fechado!')

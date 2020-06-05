# O with fecha o arquivo quando o bloco é finalizado
with open('Pessoas.csv', encoding='utf8') as arquivo:
    with open('Pessoas.txt', 'w', encoding='utf8') as saida:
        for pessoa in arquivo:
            registro = pessoa.strip().split(',')
            print('Nome: {} | Idade: {}'.format(*registro), file=saida)

if arquivo.closed:
    print('Arquivo foi fechado!')

if saida.closed:
    print('Arquivo de saída foi fechado!')

arquivo = open('Pessoas.csv', encoding='utf8')
# Lê o arquivo sob demanda, não carrega tudo na memória -> Stream

for pessoa in arquivo:
    print('Nome: {} | Idade: {}'.format(*pessoa.split(',')))

arquivo.close()

arquivo = open('Pessoas.csv', encoding='utf8')
# Todo o arquivo é carregado para variável 'dados'
dados = arquivo.read()
arquivo.close()

for pessoa in dados.splitlines():
    # print(pessoa.split(',')) -> Cria uma lista para cada pessoa -> ['Nome', 'Idade']
    print('Nome: {} | Idade: {}'.format(*pessoa.split(',')))

# Aula #19 - Dicionários

'''
Tupla = ()
Lista = []
Dicionário = {}
'''

filme = {'titulo': 'Star Wars', 'ano':1997, 'diretor':'George Lucas'}


print(filme['titulo']) # Retorna apenas o valor apontado pela chave
print(f'{filme["titulo"]} foi lançado em {filme["ano"]}.')
print(filme.values()) # Retorna todos os valores de filme. Ex.: 'Star Wars'
print(filme.keys()) # Retorna todas as chaves de filme. Ex.: 'titulo'
print(filme.items()) # Retorna todas os valores e as chaves de filme

for k, v in filme.items():
    print(f'O {k} é {v}.')

del filme['ano'] # Apaga a chave ano e seu valor 1997
print(filme)

filme['diretor'] = 'Sara' # Substitui o valor apontado pela chave diretor
print(filme)

filme['ano'] = 1997 # Adiciona chave e valor
print(filme)

brasil = []
estado1 = {'uf':'Bahia', 'sigla':'BA'}
estado2 = {'uf':'Paraíba', 'sigla':'PB'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0]['sigla'])

br = list()
estado = dict()
for i in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    br.append(estado.copy())

for est in br:
    for k, v in est.items():
        print(f'O campo {k} tem valor {v}.')

for est in br:
    for v in est.values():
        print(v, end=' ')
    print()

# Desafios 90 -> 95
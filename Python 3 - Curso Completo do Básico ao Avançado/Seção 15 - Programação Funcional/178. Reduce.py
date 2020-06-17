from functools import reduce

pessoas = [
    {'nome': 'Maria', 'idade': 20},
    {'nome': 'Sara', 'idade': 10},
    {'nome': 'Mariana', 'idade': 15},
    {'nome': 'Túlio', 'idade': 25},
    {'nome': 'Daniel', 'idade': 30},
    {'nome': 'Ana Maria', 'idade': 40}
]

# Reduce
soma_idades = reduce(lambda idades, p: idades + p['idade'], pessoas, 0)
print(soma_idades)

# Reduce + Filter
menores = filter(lambda p: p['idade'] < 18, pessoas)
soma_idades = reduce(lambda idades, p: idades + p['idade'], menores, 0)
print(soma_idades)

# Reduce + Filter + Map
so_idades = map(lambda p: p['idade'], pessoas)
menores = filter(lambda idade: idade < 18, so_idades)
soma_idades = reduce(lambda idades, atual: idades + atual, menores, 0)
print(soma_idades)

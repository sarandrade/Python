pessoas = [
    {'nome': 'Maria', 'idade': 20},
    {'nome': 'Sara', 'idade': 10},
    {'nome': 'Mariana', 'idade': 15},
    {'nome': 'Túlio', 'idade': 25},
    {'nome': 'Daniel', 'idade': 30},
    {'nome': 'Ana Maria', 'idade': 40}
]

menores = filter(lambda p: p['idade'] < 18, pessoas)
print(list(menores))

nome_grande = filter(lambda p: len(p['nome']) >= 7, pessoas)
print(list(nome_grande))

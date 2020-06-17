lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {'nome': 'Maria', 'idade': 20},
    {'nome': 'Daniel', 'idade': 30},
    {'nome': 'Ana', 'idade': 40}
]
so_nomes = map(lambda n: n['nome'], lista_2)
print(list(so_nomes))

so_idades = map(lambda n: n['idade'], lista_2)
print(list(so_idades))

so_idades = map(lambda n: n['idade'], lista_2)
print(f'Soma das idades = {sum(so_idades)}')

# Desafio: usando map retorne frases '<Nome> tem <idade> anos.'
frases = map(lambda f: f'<{f["nome"]}> tem <{f["idade"]}> anos.', lista_2)
print(list(frases))

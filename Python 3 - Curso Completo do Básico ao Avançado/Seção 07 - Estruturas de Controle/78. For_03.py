# Percorrendo dicionário
produto = {'nome': 'Caneta Bic', 'valor': 14.99, 'importada': True, 'estoque': 200}

print('Chaves: ', end='')
# for chave in produto.keys():
for chave in produto:
    print(chave, end=' ')
print()

print('Valores: ', end='')
for valor in produto.values():
    print(valor, end=' ')
print()

for chave, valor in produto.items():
    print(f'{chave} -> {valor}')

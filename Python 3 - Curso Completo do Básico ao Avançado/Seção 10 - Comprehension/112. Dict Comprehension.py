dicionario = {f'Item {i}':i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'{chave} -> {valor}')

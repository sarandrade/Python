# Desafios 87

matriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

        matriz[linha].append(num)

soma = 0
print('-+-'*10)
for linha in matriz:
    for termo in linha:
        print(f'[{termo:^4}]', end=' ')

        if termo % 2 == 0:
            soma += termo
    print()
print('-+-'*10)
print(f'Soma dos valores pares: {soma}')

soma3 = 0
for linha in matriz:
    soma3 += linha[2]
print(f'Soma dos valores da 3ª coluna: {soma3}')

maior2 = 0
for i in range(0, 3):
    if matriz[1][i] > maior2 or i == 0:
        maior2 = matriz[1][i]
print(f'Maior valor da 2ª linha: {maior2}')
# Desafios 86

matriz = [[], [], []]

for linha in range(0, 3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

        matriz[linha].append(num)

print('-+-'*10)

for linha in matriz:
    for termo in linha:
        print(f'[{termo:^4}]', end=' ')
    print()
# Desafios 85

numeros = [[], []]

for i in range(1, 8):
    num = int(input(f'Digite o {i}° valor: '))

    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print('-+-'*10)
print(f'Valores pares: {sorted(numeros[0])}')
print(f'Valores ímpares: {sorted(numeros[1])}')
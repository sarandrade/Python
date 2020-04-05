# Desafios 66

soma = 0

while True:
    num = float(input('Digite um número [99 parada]: '))

    if num == 99:
        break

    soma += num

print(f'A soma dos números digitados é {soma}')
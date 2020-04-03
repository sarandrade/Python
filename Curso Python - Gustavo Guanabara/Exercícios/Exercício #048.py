# Desafios 48

soma = 0

for i in range(1, 500, 2):
    
    if i % 3 == 0:
        soma += i

print('A soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é {}.'.format(soma))
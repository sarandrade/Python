# Desafios 48

soma = 0
cont = 0 # Contador

for i in range(1, 501, 2):
    
    if i % 3 == 0:
        cont += 1
        soma += i

print('A soma dos {} números ímpares múltiplos de 3 entre 1 e 500 é {}.'.format(cont, soma))
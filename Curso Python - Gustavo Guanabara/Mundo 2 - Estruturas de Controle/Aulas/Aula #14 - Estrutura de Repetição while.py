# Aula #14 - Estrutura de Repetição while

'''
while not condição:
    comandos
'''
c = 1

while c < 10: # Condição de parada
    print(c)
    c += 1

par = impar = 0
n = 1

while n != 0:
    n = int(input('Digite um número inteiro: '))

    if n != 0:

        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} números pares e {} números ímpares.'.format(par, impar))

# Desafios 57 -> 65
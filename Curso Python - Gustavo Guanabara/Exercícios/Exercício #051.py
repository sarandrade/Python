# Desafios 51

inicio = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

for i in range(inicio, inicio + 10 * razao, razao):
    print(i, end=' ')
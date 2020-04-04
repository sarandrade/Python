# Desafios 62

inicio = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

i = 10

while i != 0:
    print(inicio, end=' ')
    inicio = inicio + razao
    i -= 1

    if i == 0:
        opcao = int(input('\nDeseja ver mais quantos termos? '))
        i = opcao
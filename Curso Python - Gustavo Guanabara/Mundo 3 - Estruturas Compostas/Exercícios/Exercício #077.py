# Desafios 77

tupla = ('Sara', 'Tulio', 'Mari', 'Paula', 'Hellen')

for termo in tupla:
    print(f'\n{termo} => ', end='')

    for letra in termo:

        if letra in 'AEIOUaeiou':
            print(letra, end=' ')
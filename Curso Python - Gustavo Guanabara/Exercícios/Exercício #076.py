# Desafios 76

print('-'*30)
print(f'{"LISTA DE PREÇOS":^30}')
print('-'*30)

tupla = ('Caneta', 2, 'Caderno', 8, 'Livro', 20, 'Estojo', 15, 'Régua', 7.80)

for posicao, termo in enumerate(tupla):
    if posicao % 2 == 0:
        print(f'{termo:.<20}', end='R$ ')
    else:
        print(f'{termo:>7.2f}')

print('-'*30)
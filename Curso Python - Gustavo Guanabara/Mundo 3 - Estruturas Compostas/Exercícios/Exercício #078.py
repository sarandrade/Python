# Desafios 78

lista = [] 

for i in range(0,5):
    num = int(input(f'Digite um valor para a posição {i}: '))
    lista.append(num)

print('-+-'*20)
print(f'Você digitou os valores: {lista}')

maior = max(lista)
print(f'O maior valor foi {maior} nas posições', end=' ')
for posicao, termo in enumerate(lista):
    if termo == maior:
        print(posicao, end=' ')

menor = min(lista)
print(f'\nO menor valor foi {menor} nas posições', end=' ')
for posicao, termo in enumerate(lista):
    if termo == menor:
        print(posicao, end=' ')
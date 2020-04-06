# Desafios 80

lista = []

for i in range(0,5):
    num = int(input('Digite um valor: '))
    
    if i == 0:
        maior = num
        lista.append(num)
        print('O primeiro termo de sua lista foi adicionado...')
    elif num > maior:
        lista.append(num)
        maior = num
        print('O termo foi adicionado ao fim da lista...')
    else: 
        for posicao, termo in enumerate(lista):
            if num <= termo:
                lista.insert(posicao, num)
                print(f'O termo foi adicionado na posição {posicao}...')
                break

print(lista)
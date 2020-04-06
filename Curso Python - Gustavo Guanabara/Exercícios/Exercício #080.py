# Desafios 80

lista = []

for i in range(0,5):
    num = int(input(f'Digite um valor: '))
    
    if i == 0:
        maior = num
        lista.append(num)
        print('O primeiro termo de sua lista foi adicionado...')
    else:
        if num > maior:
            lista.append(num)
            maior = num
            print('O termo foi adicionado ao fim da lista...')
        else: 
            for posicao, termo in enumerate(lista):
                if posicao == 0:
                    if num < termo:
                        lista.insert(0, num)
                        print('O termo foi adicionado na posição 0...')
                print(posicao)
                print(termo)
                print(lista[posicao])
                if termo < num < lista[posicao + 1]:
                    lista.insert(posicao, num)
                    print(f'O termo foi adicionado na posição {posicao}...')

print(lista)
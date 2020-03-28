# Curso - Introdução a Linguagem Python

lista1 = [1,2,3,4,5]
lista2 = [1,2.5,'Sara',True]

print(lista2[3])

tamanho = len(lista2)
print(tamanho)

lista2.append('Túlio') # Adiciona termo à lista
print(lista2)

if 3 in lista1:
    print('3 está na lista1')

del lista1[2:] # Apaga termo da lista
print(lista1)

del lista1[:]
print(lista1)

lista3 = [125,65,24,85,36,98,1,45]

lista3.reverse() # Inverte a lista
print(lista3)

lista_ordenada = sorted(lista3) # Ordena a lista
print(lista_ordenada)

lista3.sort() # Ordena a lista
print(lista3)

lista3.sort(reverse=True) # Ordena a lista em ordem decrescente
print(lista3)

lista4 = ['Sara', 'sara', 'Mari', 'Túlio', 'Paula']

lista4.sort() # Ordena a lista em ordem alfabétia
print(lista4)

lista = [1, 3, 5]

lista[0], lista[2] = lista[2], lista[0] # Troca os termos da lista de posição

print(lista)
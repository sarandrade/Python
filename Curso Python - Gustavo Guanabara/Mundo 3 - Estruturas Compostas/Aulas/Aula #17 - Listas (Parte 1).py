# Aula #17 - Listas (Parte 1)

'''
Tuplas = ()
Listas = []
'''

lista = [2, 8, 5, 7]
print(lista)

# Substituindo elementos

lista[2] = 3 # Substitui o valor que está na posição 2
print(f'Substituindo 5 por 3: {lista}')

# Adicionando elementos

lista.append(7) # Adiciona o valor 7 no fim da lista
print(f'Adicionando o termo 7 ao fim da lista: {lista}')

lista.insert(2, 0) # Adiciona o valor 0 na posição 2
print(f'Adicionando o termo 0 na posição 2: {lista}')

for i in range(0, 3):
    lista.append(int(input('Digite um valor: ')))

# Ordenando a lista

lista.sort() # Ordena e modifica a lista
print(lista)

lista.sort(reverse=True) # Ordena a lista em ordem reversa 
print(lista) 

print(f'A lista ordenada com sorted: {sorted(lista)}') # Ordena a lista sem modificá-la
print(f'Mas como a lista não foi modificada: {lista}')

# Tamanho

print(f'A lista tem {len(lista)} termos.') # Tamanho da lista

# Removendo elementos 

del lista[0] # Remove o termo na posição 0
print(f'Removendo o primeiro termo: {lista}')

lista.pop() # Remove o último termo
print(f'Removendo o último termo: {lista}')

lista.pop(2) # Remove o termo na posição 2
print(f'Removendo o termo na posição 2: {lista}')

if 8 in lista:  
    lista.remove(8) # Remove o primeiro valor 8(conteúdo) da lista
    print(f'Removendo o primeiro 8 da lista: {lista}')
else:
    print('O número 8 não está na lista')

for posicao, termo in enumerate(lista):
    print(f'Na posição {posicao} encontrei o valor {termo}.')

# Inicializando uma lista 

lista1 = [] # Vazia
lista2 = list() # Vazia
lista3 = list(range(0, 11))
print(lista3)

# Outros

a = [1, 2, 3, 4]
b = a # Há uma ligação entre as duas listas 
b[2] = 8 # Se alterar a lista b, a lista a tbm será alterada
print(a)
print(b)

x = [1, 2, 3, 4]
y = a[:] # y recebe uma cópia dos valores de x
y[2] = 8 # Se alterar a lista y, a lista x não será alterada
print(x)
print(y)

# Desafios 78 -> 83 
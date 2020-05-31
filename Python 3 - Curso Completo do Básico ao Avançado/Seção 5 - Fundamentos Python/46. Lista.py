# print(dir(list))

lista_1 = []
lista_2 = [1, 5, 'Ana', 'Sara', 2.5]

# A lista é dinâmica -> Cresce dinamicamente
# A lista aceita tipos heterogêneos -> Aceita mais de um tipo dentro de uma lista

print(len(lista_1)) # Tamanho da lista

lista_1.append(1) # Adiciona elementos
lista_1.append(2)
print(lista_1)

lista_2.remove(5) # Remove o item '5'
print(lista_2)

lista_2.reverse() # Reverte a lista
print(lista_2)

print(lista_2.index('Sara')) # Retorna o valor do índice 

print(lista_2[1]) # Retorna o valor indicado pelo índice 1
print(lista_2[-2])

print('Ana' in lista_2)

print(lista_2[1:-1]) # Não inclui o elemento indicado pelo -1

del lista_2[0] # Apaga o elemento indicado pelo índice 0
print(lista_2)

del lista_2[1:]
print(lista_2)

'''
Conjunto (set)
    -> Não segue a ordem de inserção
    -> Não é indexado
    -> Não aceita repetição
'''

conjunto = {1, 2, 3}
print(type(conjunto))

a = set('tulio') # Cria um set com cada uma das letras
print(a)

print('l' in a, '4' not in a)

print({1, 2, 3} == {3, 2, 1, 1}) # True

# Operações
c1 = {1, 2}
c2 = {3, 2}

# União
print(c1.union(c2))

# Interseção
print(c1.intersection(c2))

# União que modifica o set c1
c1.update(c2)
print(c1)

# Verificando se um conjunto é subconjunto de outro
print(c2 <= c1) # c2 é subconjunto de c1 ? True
print(c1 >= c2) # c1 é superconjunto de c2 ? True

# Diferença entro dois conjuntos
print({1, 2, 3} - {1})

# Retirando um elemento do conjunto
c1 -= {2}
print(c1)

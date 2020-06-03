# print(dir(tuple))

tupla = () # ou -> tupla = tuple()

# A tupla é imutável, não pode ser alterada

tupla = ('um')
print(type(tupla)) # String

tupla = ('um',)
print(type(tupla)) # Tupla

cores = ('verde', 'azul', 'rosa', 'rosa')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('rosa')) # Retorna o índice do elemento 'rosa'

print(cores.count('rosa')) # Retorna quantos elementos 'rosa' tem dentro da tupla

print(len(cores)) # Tamanho da tupla

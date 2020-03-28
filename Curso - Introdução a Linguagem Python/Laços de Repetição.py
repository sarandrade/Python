# Curso - Introdução a Linguagem Python

x = 1

'''
Laços de repetição
- while condição:
- for
- for e range
'''
while x < 10:
    if x == 2:
        print(x)
    x = x + 1

lista1 = [1,2,3,4,5]
lista2 = [1,2.5,'Sara',True]

for i in lista2:
    print(i)

for i in range(5,15,2):
    print(i)

nomes = ['sara','tulio', 'mari', 'paula', 'pedro']

for nome in nomes:
    print(nome)
print()

for nome in range(0,5,2):
    print(nomes[nome])

indices = range(5)
print(indices)

for ind in indices:
    print(nomes[ind])
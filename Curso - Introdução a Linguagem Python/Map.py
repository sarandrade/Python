# Curso - Introdução a Linguagem Python

def dobro(x):
    return 2*x

x = 2
print(dobro(x))
print()

'''
Map
- map(função, lista)
'''
lista = [1,2,3,4,5]

lista_dobro = map(dobro, lista)

'''
for i in lista_dobro:
    print(i)
    
ou
'''
novaLista = list(lista_dobro)
print(novaLista)
# Curso - Introdução a Linguagem Python

a = 'Sara'
b = 'Andrade'

'''
Strings 
- string = string.método()
'''
concatenar = a + ' ' + b
print(concatenar)
print(concatenar.lower())
concatenar = concatenar.upper()
print(concatenar)

concatenar = a + ' ' + b + '\n'
print(concatenar)
print(concatenar.strip())

tamanho = len(concatenar)
print(tamanho)

print(a[2])
print(concatenar[0:8])

str = 'O rato roeu a roupa do rei de Roma'
lista = str.split()
print(lista)
lista = str.split('r')
print(lista)

busca = str.find('rei')
print(busca)
print(str[busca:])
print(str.find('rainha'))

str = str.replace('o rei', 'a rainha')
print(str)
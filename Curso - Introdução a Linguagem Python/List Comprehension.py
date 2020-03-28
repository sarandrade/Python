# Curso - Introdução a Linguagem Python

x = [1,2,3,4,5]
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)

'''
List Comprehension
z = [valor_a_adicionar laço condição]
'''
z = [i**2 for i in x]
print(z)

w = [i for i in x if i%2==1]
print(w)
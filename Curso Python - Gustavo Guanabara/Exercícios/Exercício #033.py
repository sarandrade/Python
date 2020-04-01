# Desafios 33

a, b, c = input('Digite três números diferentes: ').split()

'''
if (a > b and a > c):
    print('{} é o maior número.'.format(a))
elif b > c:
    print('{} é o maior número.'.format(b))
else:
    print('{} é o maior número.'.format(c))

if (a < b and a < c):
    print('{} é o menor número.'.format(a))
elif b < c:
    print('{} é o menor número.'.format(b))
else:
    print('{} é o menor número.'.format(c))
'''

menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior número é {}.'.format(maior))
print('O menor número é {}.'.format(menor))
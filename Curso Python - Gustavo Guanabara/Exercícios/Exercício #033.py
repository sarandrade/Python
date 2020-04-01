# Desafios 33

a, b, c = input('Digite três números diferentes: ').split()

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
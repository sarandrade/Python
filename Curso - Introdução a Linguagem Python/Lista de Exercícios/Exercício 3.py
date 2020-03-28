# Curso - Introdução a Linguagem Python

a = int(input('Termo que acompanha x^2: '))
b = int(input('Termo que acompanha x: '))
c = int(input('Termo que independente: '))

'''
a, b, c = input('Digite os três termos da equação de segundo grau: ').split()

print('{} {} {}'.format(a, b, c))
'''
delta = b**2 -4*a*c

r_1 = (-b + delta**(1/2))/2*a
r_2 = (-b - delta**(1/2))/2*a


print('As raizes da equação de segundo grau são: {r1:.1f} e {r2:.1f}'.format(r1 = r_1, r2 = r_2))
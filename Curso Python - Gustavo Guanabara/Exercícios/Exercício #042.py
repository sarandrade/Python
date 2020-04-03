# Desafios 42

r1 = float(input('Digite o valor do primeiro lado: '))
r2 = float(input('Digite o valor do segundo lado: '))
r3 = float(input('Digite o valor do terceiro lado: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    
    print('Os lados escolhidos formam um triângulo.')
    
    if r1 == r2 == r3:
        print('Triângulo Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Triângulo Escaleno.')
    else: 
        print('Isósceles.')

else:
    print('Os lados escolhidos NÃO formam um triângulo.')
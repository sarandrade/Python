# Desafios 96

def area(a, b):
    area = a * b
    print(f'\nA área de um terreno {a} x {b} é de {area} m².')

print('-+-'*8)
print(' Controle de Terrenos')
print('-+-'*8)

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

area(l, c)
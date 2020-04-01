# Desafios 35

lista = input('Digite os valores dos três lados: ').split() 

r1 = float(lista[0])
r2 = float(lista[1])
r3 = float(lista[2])

print(r1)
print(r2)
print(r3)

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('É possível for um triângulo com esses lados.')
else:
    print('Não é possível for um triângulo com esses lados.')
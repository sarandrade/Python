# List Comprehension
# [ expressão for item in list]

dobro = [i * 2 for i in range(10)]
print(dobro)

# Versão sem o List Comprehension
dobro = []
for i in range(10):
    dobro.append(i * 2)
print(dobro)

# List Comprehension utilizando condicional
# [ expressão for item in list if condicional ]
dobro_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobro_pares)

# Versão sem o List Comprehension
dobro_pares = []
for i in range(10):
    if i % 2 == 0:
        dobro_pares.append(i * 2)
print(dobro_pares)

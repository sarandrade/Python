# Generator consome menos memória que o List Comprehension
# List Comprehension gera a lista completa -> []
# Generator gera a lista sob demanda -> ()
generator = (i ** 2 for i in range(10) if i % 2 ==0)

print(next(generator)) # Saída 0
print(next(generator)) # Saída 4
print(next(generator)) # Saída 16
print(next(generator)) # Saída 36
print(next(generator)) # Saída 64
# print(next(generator)) -> Erro!

'''
# Outra Alternativa

for numero in generator:
    print(numero)
'''

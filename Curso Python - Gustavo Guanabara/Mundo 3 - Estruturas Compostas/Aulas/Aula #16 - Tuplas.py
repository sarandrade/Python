# Aula #16 - Tuplas 

'''
Variáveis Compostas

=> Tuplas
=> Listas
=> Dicionários
----

- Tuplas são imutáveis
'''

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim ')# Com ou sem parênteses 
print(lanche)
print(len(lanche)) # Retorna o tamanho da tupla
print(lanche[2]) # Retorna o segundo termo da tupla
print(lanche[-1]) # Retorna o último termo da tupla
print(lanche[1:3]) # Retorna do elemento 1 até o elemento 2
print(lanche[-2:]) # Retorna do elemento 3 até o fim
print(sorted(lanche)) # Coloca a tupla em ordem 

for comida in lanche:
    print(f'Vou comer {comida}')

for i, comida in enumerate(lanche):
    print(i)
    print(f'Vou comer {comida}')

for i in range(0, len(lanche)):
    print(i)
    print(f'Vou comer {lanche[i]}')

a = (1, 2, 3, 4, 5)
b = (4, 5, 6)
c = a + b
print(c)
print(c.count(5)) # Conta quantas vezes aparece o número 5 na tupla
print(c.index(5)) # Retorna a posição do número 5 na tupla
print(c.index(5, 5)) # Retorna a posição do número 5 na tupla a partir da posição 5

pessoa = ('Sara', 21, 'F', 60)
del(pessoa) # Apaga toda a tupla

# Desafios 72 -> 77
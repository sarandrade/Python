# Aula #20 - Funções (Parte 1)

def linha():
    print('-+-'*5)

linha()
print(' Sara')
linha()
print('Andrade')
linha()
print(' Dias')
linha()

def mensagem(msg):
    print('-+-'*5)
    print(msg)

mensagem(' Sara')
mensagem('Andrade')
mensagem(' Dias')

def soma(a, b):
    s = a + b
    print(f'A = {a}; B = {b}')
    print(f'Soma = {s}')

soma(9, 8)
soma(b = 5, a = 4)

def sum(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'A soma dos valores {valores} é {s}')

sum(5, 8, 9)
sum(2, 4, 7, 8, 5)

def contador(*num):
    print(f'Total de parâmetros: {len(num)}')
    print(f'Parâmetros: {num}')

contador(1, 2, 3)
contador(9, 8, 7, 5, 4)

def dobra(lista):
    i = 0
    while i < len(lista):
        lista[i] *= 2
        i += 1

valores = [1, 2, 3, 4, 5]
dobra(valores)
print(valores)

# Desafios 96 -> 100
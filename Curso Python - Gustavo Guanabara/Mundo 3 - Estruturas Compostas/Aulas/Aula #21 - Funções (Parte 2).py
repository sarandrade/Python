# Aula #21 - Funções (Parte 2)

# -> Interactive help

help(print)
print(print.__doc__)

# -> Docstrings

def contador(i, f, c):
    """
    -> Faz uma contagem e mostra na tela
        :param i: início da contagem
        :param f: fim da contagem
        :param c: passo da contagem
        :return: sem retorno
    """
    c = i
    while c <= f:
        print(c, end=' ') 
        c +=print
    print('\nFim!!')

help(contador)

# -> Argumentos opcionais

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'Soma = {s}')

somar(2, 5, 8)
somar(8, 5)
somar(5)
somar()

# -> Escopo de variáveis

'''
- Variável local / Escopo local
- Variável global / Escopo global
'''

def funcao1():
    n1 = 100
    print(f'n1 dentro vale {n1}.')

def funcao2():
    global n1
    n1 = 5
    print(f'n1 dentro vale {n1}.')

n1 = 1
funcao1()
funcao2()
print(f'n1 fora vale {n1}.')

# -> Retorno de resultados

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s
    

s1 = somar(2, 5, 8)
s2 = somar(8, 5)

print(f'As somas valem {s1} e {s2}.')

# Exercício Prático 1

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

num = int(input('Digite um número: '))
print(f'O fatorial de {num} é {fatorial(num)}')

# Exercício Prático 2

def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
print('É par!' if par(num) else 'É ímapar!')

# Desafios 101 -> 106
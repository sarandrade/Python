# Curso - Introdução a Linguagem Python

a, b, sinal = input('Digite os números e um sinal: ').split()

a = int(a)
b = int(b)

if sinal == '+':
    print(a+b)
elif sinal == '-':
    print(a-b)
elif sinal == '/':
    print(a/b)
elif sinal == '*':
    print(a*b)
else:
    print('Vai dar não')
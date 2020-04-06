# Desafios 83

exp = input('Digite uma expressão: ')
lista = list(exp)

paren1 = paren2 = 0
for i in lista:
    if i == '(':
        paren1 += 1
    elif i == ')':
        paren2 += 1

if paren1 == paren2:
    print('Expressão Válida!')
else:
    print('Expressão Inválida!')
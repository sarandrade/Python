# Aula #12 - Condições Aninhadas

'''
- Estrutura Condicional Aninhada

if condição_1:
    função_1
elif condição_2:
    função_2
else:
    função_3
'''
nome = input('Qual seu nome? ')

if nome == 'Sara':
    print('Que nome lindo!')
elif nome == 'Túlio':
    print('Que nome diferente.')
elif nome in 'Mari Paula Pedro':
    print('Muito popular o seu nome!')
else:
    print('Nome legal!')
print('Bom dia, {}.'.format(nome))

# Desafios 36 -> 45
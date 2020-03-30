# Aula #07 - Operadores Aritméticos

'''
Operadores diferentes
- ** => Potência 
- // => Divisão inteira (Parte inteira da divisão)
- % => Resto da divisão

Ordem de Precedência 
- 1 => ()
- 2 => **
- 3 => *, /, //, %
- 4 => +, -
'''
pot = pow(4, 2)
print(pot)

nome = input('Qual seu nome? ')

print('Seja \nbem vindo,\n {:>20}!'.format(nome)) # Alinhado a direita 
print('Seja bem vindo, {:<20}!'.format(nome)) # Alinhado a esquerda
print('Seja bem vindo, {:^20}!'.format(nome), end=' >>> ') # Alinhado ao centro 
print('Seja bem vindo, {:=^20}!'.format(nome)) 

# Desafios 05 -> 15
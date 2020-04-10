# Aula #10 - Condições

'''
if condição:
    comando_1
else:
    comando_2

ou 

print('Mensagem_1' if condição else 'Mensagem_2')
'''

nome = input('Qual seu nome? ')

# Condição Simples 
if nome == 'Sara':
    print('Que nome lindo!')
print('Bom dia, {}.'.format(nome))

# Condição Composta 
if nome == 'Sara':
    print('Que nome lindo!')
else:
    print('Nome legal!')
print('Bom dia, {}.'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

med = (n1 + n2)/2

print('Sua média foi {}.'.format(med))

# Condição Simplificada
print('Parabéns!!' if med >= 7 else 'Estude mais!!')

# Desafios 28 -> 35
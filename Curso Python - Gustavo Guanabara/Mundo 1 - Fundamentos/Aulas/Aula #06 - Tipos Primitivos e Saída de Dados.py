# Aula #06 - Tipos Primitivos e Saída de Dados

'''
 Tipos Primitivos 

 - int => números inteiros 
 - float => números reais ou de ponto flutuante 
 - bool => valores lógicos ou booleanos (True ou False)
 - str => valores caracteres ou strings ('string')
'''

num1 = input('Digite o primeiro número: ')
num2 = float(input('Digite o segundo número: '))

print(type(num1))
print(type(num2))

print(num1.isnumeric()) # Checa se o valor na string é um número
print(num1.isalpha()) # Checa se o valor na string é uma letra

soma = float(num1) + num2

print('Soma entre {} e {} vale: {:.1f}'.format(num1, num2, soma))

# Desafio 04
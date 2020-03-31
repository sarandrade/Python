# Desafios 25

nome = input('Digite seu nome: ').upper()

x = nome.find('DIAS')

if x == -1:
    print('Esse nome não tem a palavra Dias.')
else:
    print('Esse nome tem a palavra Dias.') 
# Desafios 43

peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em m²: '))

imc = peso / altura

if imc <= 18.5:
    print('Abaixo do peso.')
elif imc <= 25:
    print('Peso ideal.')
elif imc <= 30:
    print('Sobrepeso.')
elif imc <= 40:
    print('Obeso.')
else: 
    print('Obesidade Mórbida.') 
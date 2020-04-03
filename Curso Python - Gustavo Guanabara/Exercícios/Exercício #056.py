# Desafios 56

soma = 0
velho = 0
mulher = 0

for i in range(0, 4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo: ').upper()

    soma += idade

    if sexo == 'MASCULINO':

        if idade > velho:
            velho = idade 
            homem = nome

    elif sexo == 'FEMININO':

        if idade < 20:
            mulher += 1

print('A média de idade é {} anos.'.format(soma/4))
print('O homem mais velho se chama {}.'.format(homem))
print('{} mulheres têm menos de 20 anos.'.format(mulher))
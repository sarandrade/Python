# Desafios 56

soma = 0
velho = 0
mulher = 0
homem = ''

for i in range(1, 5):
    print('{} {}ª Pessoa {}'.format('-' * 5, i, '-' * 5))
    nome = input('Digite o nome: ').strip()
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [F/M]: ').upper().strip()

    soma += idade

    if sexo == 'M':

        if idade > velho:
            velho = idade 
            homem = nome

    elif sexo == 'F':

        if idade < 20:
            mulher += 1

print('A média de idade é {} anos.'.format(soma/4))

if homem == '':
    print('Nenhum homem foi cadastrado.')
else:
    print('O homem mais velho se chama {}.'.format(homem))

if mulher == 0:
    print('Nenhuma mulher tem menos de 20 anos.')
elif mulher == 1:
    print('Apenas 1 mulher tem menos de 20 anos.')
else:
    print('{} mulheres têm menos de 20 anos.'.format(mulher))
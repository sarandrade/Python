# Aula #15 - Interrompendo Repetições while

'''
while True:
    if subcondição_1:
        comando_1
    if subcondição_2:
        comando_2
        break
'''
soma = 0

while True:
    num = int(input('Digite um número: '))

    if num == 999:
        break

    soma += num
#print('A soma dos termos vale {}'.format(soma))
print(f'A soma vale {soma}')

nome = 'Sara'
idade = 21

print(f'{nome} tem {idade} anos.') # Python 3.6+
print('{} tem {} anos.'.format(nome, idade)) # Python 3
print('%s tem %d anos.' % (nome, idade)) # Python 2

# Desafios 66 -> 71
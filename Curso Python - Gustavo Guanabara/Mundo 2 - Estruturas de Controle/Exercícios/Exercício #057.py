# Desafios 57

sexo = 'A'

while not (sexo == 'M' or sexo == 'F'):
    sexo = input('Digite o seu sexo [F/M]: ').upper().strip()[0]

print('Muito Obrigada!!')

'''
ou 

sexo = input('Digite o seu sexo [F/M]: ').upper().strip()[0]

while sexo not in 'MF':
    sexo = input('Dados inválidos. \nPor favor, digite o seu sexo [F/M]: ').upper().strip()[0]

print('Muito Obrigada!!')
'''
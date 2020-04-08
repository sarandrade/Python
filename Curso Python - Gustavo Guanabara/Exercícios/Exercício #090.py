# Desafios 90

aluno = {}

aluno['Nome'] = input('Nome: ')
aluno['Média'] = int(input(f'Média de {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] >= 5:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

print('-+-'*10)
for k, v in aluno.items():
    print(f'{k} = {v}') 
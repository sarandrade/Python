# Desafios 105

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
        :paran n: uma ou mais notas dos alunos (aceita várias)
        :paran sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma ou aluno.
    """
    dic = {}
    print('-+-'*25)
    dic['Total'] = len(n) 
    dic['Maior'] = max(n)
    dic['Menor'] = min(n)
    dic['Média'] = sum(n) / len(n)

    if sit:
        if dic['Média'] >= 7:
            dic['Situação'] = 'Ótimo'
        elif dic['Média'] >= 5:
            dic['Situação'] = 'Razoável'
        else:
            dic['Situação'] = 'Ruim'

    return dic

resp = notas(5.5, 9.5, 4, 2, 1, 6.5, sit=True)
print(resp)

help(notas)

'''
==> Como eu fiz...

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
        :paran n: uma ou mais notas dos alunos (aceita várias)
        :paran sit: valor opcional, indicando se deve ou não adicionar a situação
        :return: dicionário com várias informações sobre a situação da turma ou aluno.
    """
    print('-+-'*25)
    soma = 0
    for i in range(0, len(n)):
        soma += n[i]

        if i == 0 or n[i] > maior:
            maior = n[i]
        if i == 0 or n[i] < menor:
            menor = n[i]

    media = soma / len(n)
    
    if sit:
        if media >= 7:
            s = 'Ótimo'
        elif media >= 5:
            s = 'Razoável'
        else:
            s = 'Ruim'

        dic = {'Total':len(n), 
            'Maior':maior,
            'Menor':menor,
            'Média':media,
            'Situação':s}
    else:
        dic = {'Total':len(n), 
            'Maior':maior,
            'Menor':menor,
            'Média':media}
    
    return dic

resp = notas(5.5, 9.5, 4, 2, 1, 6.5, sit=True)
print(resp)

help(notas)
'''
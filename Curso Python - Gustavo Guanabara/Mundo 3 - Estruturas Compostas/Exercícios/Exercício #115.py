# Desafios 115

from modulo115 import *

arquivo = 'arquivo_115.txt'

if not ExisteArq(arquivo):
    CriarArq(arquivo)

while True:

    lstmenu = ['Ver pessoas cadastradas', 'Cadastradar nova pessoa', 'Sair do sistema']
    opc = menu(lstmenu)

    if opc == 1:
        LerArq(arquivo)

    elif opc == 2:
        print('-'*40)
        print(f'{"NOVO CADASTRO":^40}')
        print('-'*40)
        nome = input('Nome: ')
        idade = leiaint('Idade: ')
        cadastrar(arquivo, nome, idade)

    elif opc == 3:
        print('-'*40)
        print(f'{"Saindo do Sistema... Até logo!":^40}')
        print('-'*40)
        break

    else:
        print('\033[31mERRO: escolha uma opção válida (1, 2 ou 3).\033[m') 
# Módulo para o Exercício #115

def leiaint(str):
    while True:
        try:
            opc = int(input(str))
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return opc

def menu(lista):
    print('-'*40)
    print(F'{"MENU PRINCIPAL":^40}')
    print('-'*40)

    for pos, item in enumerate(lista):
        print(f'\033[33m{pos + 1} - \033[34m{item}\033[m')
    print('-'*40)

    opc = leiaint('\033[33mSua opção: \033[m')
    return opc

def ExisteArq(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def CriarArq(nome):
    try:
        a = open(nome, 'w+')
        a.close()
    except:
        print('\033[31mHouve um ERRO na criação do arquivo.\033[m')
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso!\033[m')

def LerArq(nome):
    try:
        a = open(nome, 'r')
    except:
        print('\033[31mERRO ao ler arquivo.\033[m')
    else:
        print('-'*40)
        print(f'{"PESSOAS CADASTRADAS":^40}')
        print('-'*40)
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>5} anos')
    finally:
        a.close()

def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'a')
    except:
        print('\033[31mERRO na abertura do arquivo.\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mERRO ao escrever os dados no arquivo.\033[m')
        else:
            print(f'\033[32m{nome} cadastrado(a) com sucesso!\033[m')
            a.close()
# Desafios 113

def leiaint(str):
    while True:
        try:
            num = int(input(str))
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        except:
            print(f'\033[31mERRO: Por favor, digite um número inteiro válido!\033[m')
            continue
        else:
            return num

def leiafloat(str):
    while True:
        try:
            num = float(input(str))
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        except:
            print(f'\033[31mERRO: Por favor, digite um número real válido!\033[m')
            continue
        else:
            return num

print('-+-'*10)
num = leiaint('Digite um número inteiro: ')
flo = leiafloat('Digite um número real: ')
print(f'Os números digitados foram {num} e {flo}')
print('-+-'*10)
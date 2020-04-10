# Desafios 104

def leiaint(str):
    while True:
        print('-+-'*8)
        n = input(str).strip()

        if n.isnumeric():
            return n
            break
        else:
            print('\033[31mErro! Digite um número inteiro!\033[m')

n = leiaint('Digite um número: ')
print(f'Número digitado: {n}')
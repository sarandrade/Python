# Desafios 106

def alinhar(str):
    tam = len(str) + 4
    print('~'*tam)
    print(f'  {str}')
    print('~'*tam)

def ajuda(opc):
    print()
    alinhar(f'Acessando o manual do comando {opc}...')
    help(opc)

opc = ''
while opc.upper() != 'FIM':
    alinhar('SISTEMA DE AJUDA')

    opc = input('Função ou Biblioteca > ')
    
    if opc.upper() != 'FIM':
        ajuda(opc)

alinhar('ATÉ LOGO!')
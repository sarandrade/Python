# Módulo do Exercício #107

def metade(num=0, sit=False):
    if sit:
        return moeda(num / 2)
    else:
        return num / 2

def dobro(num=0, sit=False):
    if sit:
        return moeda(num * 2)
    else:
        return num * 2

def aumentar(num=0, p=0, sit=False):
    if sit:
        return moeda(num * (1 + p/100))
    else:
        return num * (1 + p/100)

def diminuir(num=0, p=0, sit=False):
    if sit:
        return moeda(num * (1 - p/100))
    else:
        return num * (1 - p/100)

def moeda(num=0, moeda='R$'):
    return f"{moeda} {num:.2f}".replace('.',',')

def resumo(num=0, tx1=0, tx2=0):
    print('-'*35)
    print('    RESUMO DO VALOR')
    print('-'*35)
    print(f'{"Preço analisado:":<20}{moeda(num):>15}')
    print(f'{"Dobro do preço:":<20}{dobro(num, True):>15}')
    print(f'{"Metade do preço:":<20}{metade(num, True):>15}')
    print(f'{tx1:>2}{"% de aumento:":<18}{aumentar(num, tx1, True):>15}')
    print(f'{tx2:>2}{"% de redução:":<18}{diminuir(num, tx2, True):>15}')
    print('-'*35)
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
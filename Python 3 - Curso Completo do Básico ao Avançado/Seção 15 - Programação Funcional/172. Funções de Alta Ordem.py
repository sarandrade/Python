def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2 


def processar(titulo, lista, funcao):
    print(f'Processando: {titulo}')
    for i in lista:
        print(i, '=>', funcao(i))


if __name__ == "__main__":
    processar('Dobros de 1 até 10', range(1, 11), dobro)
    processar('Quadrado de 1 até 10', range(1, 11), quadrado)

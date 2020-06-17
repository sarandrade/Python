# Minha versão

def mdc(numeros):
    divisores = list(map(divisor, numeros))

    valor_mdc = max(intersecao(divisores))

    return valor_mdc


def divisor(numero):
    return list(n for n in range(1, numero + 1) if numero % n == 0)


def intersecao(divisores):
    lista = []
    for i in range(1, len(divisores)):
        inter = (set(divisores[i - 1]).intersection(divisores[i]))
        lista.append(list(inter))

    if len(lista) == 1:
        return lista[0]

    else:
        return intersecao(lista)


if __name__ == "__main__":
    print(mdc([21, 7])) # 7
    print(mdc([125, 40])) # 5
    print(mdc([9, 564, 66, 3])) # 3
    print(mdc([55, 22])) # 11
    print(mdc([15, 150])) # 15
    print(mdc([7, 9])) # 1

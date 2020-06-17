# Implementação simplificada do Map

def mapear1(funcao, lista):
    for n in lista:
        yield funcao(n)


if __name__ == "__main__":
    print(list(mapear1(lambda x: x ** 2, [2, 3, 4])))

    resultado = mapear1(lambda x: x ** 2, [2, 3, 4])
    print(next(resultado))
    print(next(resultado))
    print(next(resultado))

# Outra Alternativa

def mapear2(funcao, lista):
    return (funcao(n) for n in lista)


if __name__ == "__main__":
    print(list(mapear2(lambda x: x ** 2, [2, 3, 4])))

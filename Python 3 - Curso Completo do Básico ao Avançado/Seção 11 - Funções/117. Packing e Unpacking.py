def soma_n(*numeros): # Tupla
    soma = 0
    for n in numeros:
        soma += n

    return soma


def soma_3(a, b, c):
    return a + b + c


if __name__ == '__main__':
    # Packing
    # Pega os parâmetros e empacota dentro de uma tupla
    print(soma_n(2, 3))
    print(soma_n(2, 3, 4))
    print(soma_n(2))
    print(soma_n(2, 3, 4, 5, 6))

    # Unpacking
    # Desempacota a tupla/lista e passa os elementos como parâmetro
    tupla_numeros = (1, 2, 3)
    print(soma_n(*tupla_numeros))

    lista_numeros = [1, 2, 3]
    print(soma_n(*lista_numeros))

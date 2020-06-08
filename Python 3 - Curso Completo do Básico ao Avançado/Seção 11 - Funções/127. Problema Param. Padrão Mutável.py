def fibonacci(sequencia=[0, 1]):
    # Uso de objetos mutáveis como valor default (armadilha)
    sequencia.append(sequencia[-1] + sequencia[-2])

    return sequencia


if __name__ == "__main__":
    inicio = fibonacci()
    print(inicio, id(inicio))
    print(fibonacci(inicio))
    restart = fibonacci() # Não cria uma nova lista
    print(restart, id(restart))
    # inicio e restart tem o mesmo id - são o mesmo objeto em memória
    assert restart == [0, 1, 1]

# Sequência de Fibinacci utilizando a função sum()
# 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(quantidade):
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if quantidade == len(resultado):
            break

    return resultado

if __name__ == '__main__':
    # Lista os 15 primeiros números da sequência
    for valor in fibonacci(15):
        print(valor, end=', ')

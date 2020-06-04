# Sequência de Fibinacci utilizando a função sum()
# 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(quantidade):
    resultado = [0, 1]
    # '_' -> Variável não é usada 
    for _ in range(quantidade - 2):
        resultado.append(sum(resultado[-2:]))

    return resultado


if __name__ == '__main__':
    # Lista os 15 primeiros números da sequência
    for valor in fibonacci(15):
        print(valor, end=', ')

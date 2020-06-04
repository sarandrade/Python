# Sequência de Fibinacci utilizando Lista
# 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-1] + resultado[-2])
    return resultado

if __name__ == '__main__':
    for valor in fibonacci(150):
        print(valor, end=', ')

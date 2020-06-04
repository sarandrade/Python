# Sequência de Fibinacci utilizando a função sum()
# 0, 1, 1, 2, 3, 5, 8, 13...

def fibonacci(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(sum(resultado[-2:]))
    return resultado

if __name__ == '__main__':
    for valor in fibonacci(150):
        print(valor, end=', ')

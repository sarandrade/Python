# Sequência de Fibinacci utilizando recursividade
# 0, 1, 1, 2, 3, 5, 8, 13...
'''
def fibonacci(quantidade, resultado=(0, 1)):
    if len(resultado) < quantidade:
        return fibonacci(quantidade, resultado + (sum(resultado[-2:]),))

    return resultado

'''
def fibonacci(quantidade, resultado=(0, 1)):
    return resultado if len(resultado) == quantidade else fibonacci(quantidade, resultado + (sum(resultado[-2:]),))


if __name__ == '__main__':
    # Lista os 15 primeiros números da sequência
    for valor in fibonacci(15):
        print(valor, end=', ')

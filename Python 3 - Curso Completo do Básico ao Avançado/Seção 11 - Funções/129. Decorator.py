# Função com uma função interna
'''
def soma(a, b):
    def soma_c(c):
        return a + b + c
    return soma_c


soma_5 = soma(2, 3)
print(soma_5(50))
print(soma(1, 2)(3))
'''

# Decorator
def log(function):
    def decorator(*args, **kwargs):
        print(f'Início da chamada da função: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'O resultado da chamada: {resultado}')
        return resultado
    return decorator


@log
def soma(x, y):
    return x + y


@log
def sub(x, y):
    return x - y


if __name__ == "__main__":
    soma(5, 7)
    sub(5, y=7)

# Desafios 102

def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
        :paran num: O número a ser calculado
        :paran show: (opcional) Mostra ou não a conta
        :return: O valor do fatorial de um número num
    """
    print(f'{num}! = ', end='')
    f = 1

    if show:
        while num > 1:
            print(f'{num} x ', end='')
            f *= num
            num -= 1
        if num == 1: 
            print(f'{num} = {f}')
    else:
        while num >= 1:
            f *= num
            num -= 1
        print(f'{f}')

print()
print('-+-'*10)
fatorial(5, True)
print('-+-'*10)
print()

help(fatorial)
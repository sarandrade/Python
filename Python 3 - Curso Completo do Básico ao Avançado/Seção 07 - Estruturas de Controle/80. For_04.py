from random import randint


def sortear():
    return randint(1, 6)


if __name__ == '__main__':
    for numero_escolhido in range(1, 7):

        if numero_escolhido % 2 == 1:
            continue
        elif numero_escolhido == sortear():
            print('Acertou!!!')
            print(f'O número sorteado foi {numero_escolhido}.')
            break
        else:
            print('Não acertou o número :(')

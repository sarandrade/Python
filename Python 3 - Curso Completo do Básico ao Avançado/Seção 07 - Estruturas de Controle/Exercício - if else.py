# Exercício - if else

class TerminalColor:
    erro = '\033[91m'
    normal = '\033[0m'


def ClasseNota():
    nota = float(input('Digite sua nota (0 a 10): '))

    if nota > 10:
        print(TerminalColor.erro + 'Nota Inválida!' + TerminalColor.normal)

    elif nota > 9:
        print(f'Nota -> A')

    elif nota > 8:
        print(f'Nota -> -A')

    elif nota > 7:
        print(f'Nota -> B')

    elif nota > 6:
        print(f'Nota -> -B')

    elif nota > 5:
        print(f'Nota -> C')

    elif nota > 4:
        print(f'Nota -> -C')

    elif nota > 3:
        print(f'Nota -> D')

    elif nota > 2:
        print(f'Nota -> -D')

    elif nota > 1:
        print(f'Nota -> E')

    elif nota >= 0:
        print(f'Nota -> -E')

    else:
        print(TerminalColor.erro + 'Nota Inválida!' + TerminalColor.normal)


if __name__ == '__main__':
    ClasseNota()
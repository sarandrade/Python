# Desafios 63

num = int(input('Digite um número inteiro: '))

print('0 -> 1 -> ', end='')

seq1 = 0
seq2 = 1

while num != 2:
    termo = seq1 + seq2

    seq1 = seq2
    seq2 = termo
    num -= 1

    if num == 2:
        print('{}'.format(termo), end='')
    else:
        print('{} -> '.format(termo), end='')
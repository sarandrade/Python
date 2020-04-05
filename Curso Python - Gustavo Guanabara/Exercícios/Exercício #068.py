# Desafios 68

from random import randint

print('-=-'*20)
print('Vamos jogar par ou ímpar?')
print('-=-'*20)

cont = 0

while True:
    num = int(input('Digite um valor [0->10]: '))
    jogador = input('Par ou Ímpar [P/I]? ').upper().strip()
    print('-=-'*20)

    casa = randint(0, 10)

    soma = num + casa

    if soma % 2 == 0:
        if jogador == 'P':
            print(f'Jogador X Computador \n[ {num} ] + [ {casa} ] = [ {soma} ] \nO número {soma} é PAR! \n-=- VENCEU -=-')
            print('-=-'*20)
            cont += 1
        elif jogador == 'I':
            print(f'Jogador X Computador \n[ {num} ] + [ {casa} ] = [ {soma} ] \nO número {soma} é PAR! \n-=- PERDEU -=-')
            break
        else:
            print('Opção Inválida! Tente de novo!!')
            print('-=-'*20)
    
    else:
        if jogador == 'P':
            print(f'Jogador X Computador \n[ {num} ] + [ {casa} ] = [ {soma} ] \nO número {soma} é ÍMPAR! \n-=- PERDEU -=-')
            break
        elif jogador == 'I':
            print(f'Jogador X Computador \n[ {num} ] + [ {casa} ] = [ {soma} ] \nO número {soma} é ÍMPAR! \n-=- VENCEU -=-')
            print('-=-'*20)
            cont += 1
        else:
            print('Opção Inválida! Tente de novo!!')
            print('-=-'*20)

print('-=-'*20)
print(f'GAME OVER! Você ganhou {cont} vezes!')
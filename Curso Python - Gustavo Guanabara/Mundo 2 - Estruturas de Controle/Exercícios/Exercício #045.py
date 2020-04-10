# Desafios 45

import random
from time import sleep

print('{} Vamos jogar! {} \n'.format('-+-'*5 , '-+-'*5))

pessoa = input('Pedra, Papael ou Tesoura? ').upper().strip()

lista = ['PEDRA', 'PAPEL', 'TESOURA']

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)

casa = random.choice(lista)

print('-+-'*15)

if pessoa != 'PEDRA' and pessoa != 'PAPEL' and pessoa != 'TESOURA':
    print('Opção inválida!')

elif casa == 'PEDRA': 

    if pessoa == 'PAPEL':
        print('''Computador X Jogador 
        \n[ Pedra ] X [ Papel ] => Papel ganha!!!
        \nParabéns você ganhou!!''')
    elif pessoa == 'TESOURA':
        print('''Computador X Jogador 
        \n[ Pedra ] X [ Tesoura ] => Pedra ganha!!!
        \nPerdeuuu!!''')
    elif casa == pessoa:
        print('''Computador X Jogador 
        \n[ Pedra ] X [ Pedra ] => Empate!!!
        \nTente de novo!!''')

elif casa == 'PAPEL':

    if pessoa == 'PEDRA':
        print('''Computador X Jogador 
        \n[ Papel ] X [ Pedra ] => Papel ganha!!!
        \nPerdeuuu!!''')
    elif pessoa == 'TESOURA':
        print('''Computador X Jogador 
        \n[ Papel ] X [ Tesoura ] => Tesoura ganha!!!
        \nParabéns você ganhou!!''')
    elif casa == pessoa:
        print('''Computador X Jogador 
        \n[ Papel ] X [ Papel ] => Empate!!!
        \nTente de novo!!''')

elif casa == 'TESOURA':

    if pessoa == 'PEDRA':
        print('''Computador X Jogador 
        \n[ Tesoura ] X [ Pedra ] => Pedra ganha!!!
        \nParabéns você ganhou!!''')
    elif pessoa == 'PAPEL':
        print('''Computador X Jogador 
        \n[ Tesoura ] X [ Papel ] => Tesoura ganha!!!
        \nPerdeuuu!!''')
    elif casa == pessoa:
        print('''Computador X Jogador 
        \n[ Tesoura ] X [ Tesoura ] => Empate!!!
        \nTente de novo!!''')    
    
print('-+-'*15)
# Desafios 45

import random
print('Vamos jogar!')

pessoa = input('Pedra, Papael ou Tesoura? ').upper().strip()

lista = ['PEDRA', 'PAPEL', 'TESOURA']

casa = random.choice(lista)

print('-+-'*15)

if casa == 'PEDRA' and pessoa == 'PAPEL':
    print('''Computador X Jogador 
    \n[ Pedra ] X [ Papel ] => Papel ganha!!!
    \nParabéns você ganhou!!''')
elif casa == 'PEDRA' and pessoa == 'TESOURA':
    print('''Computador X Jogador 
    \n[ Pedra ] X [ Tesoura ] => Pedra ganha!!!
    \nPerdeuuu!!''')
elif casa == 'PAPEL' and pessoa == 'PEDRA':
    print('''Computador X Jogador 
    \n[ Papel ] X [ Pedra ] => Papel ganha!!!
    \nPerdeuuu!!''')
elif casa == 'PAPEL' and pessoa == 'TESOURA':
    print('''Computador X Jogador 
    \n[ Papel ] X [ Tesoura ] => Tesoura ganha!!!
    \nParabéns você ganhou!!''')
elif casa == 'TESOURA' and pessoa == 'PEDRA':
    print('''Computador X Jogador 
    \n[ Tesoura ] X [ Pedra ] => Pedra ganha!!!
    \nParabéns você ganhou!!''')
elif casa == 'TESOURA' and pessoa == 'PAPEL':
    print('''Computador X Jogador 
    \n[ Tesoura ] X [ Papel ] => Tesoura ganha!!!
    \nPerdeuuu!!''')
elif casa == pessoa:
    print('''Computador X Jogador 
    \n[ {} ] X [ {} ] => Empate!!!
    \nTente de novo!!'''.format(casa, pessoa))
else:
    print('Opção inválida!')
    
print('-+-'*15)
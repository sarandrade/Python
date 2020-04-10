# Desafios 93

dic = {}
lista = []

dic['nome'] = input('Nome do Jogador: ')

part = int(input(f'Quantas partidas {dic["nome"]} jogou? '))

for i in range(1, part +1):
    gol = int(input(f'Quantos gols na partida {i}? '))
    lista.append(gol)

dic['gols'] = lista
dic['total'] = sum(lista)

print('-+-'*15)
print(f'O jogador {dic["nome"]} jogou {part} partidas: \n')
for pos, gol in enumerate(lista):
    print(f'    ==> Na partida {pos + 1}, fez {gol} gols.')
print(f'\nFoi um total de {dic["total"]} gols.')
print('-+-'*15)
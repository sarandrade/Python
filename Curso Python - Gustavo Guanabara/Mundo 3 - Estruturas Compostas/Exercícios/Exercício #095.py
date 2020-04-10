# Desafios 95

dic = {}
gols = []
jogadores = []

while True:
    print('-+-'*15)
    dic.clear()
    gols.clear()
    dic['nome'] = input('Nome do Jogador: ')

    part = int(input(f'Quantas partidas {dic["nome"]} jogou? '))

    for i in range(1, part +1):
        gol = int(input(f'  Quantos gols na partida {i}? '))
        gols.append(gol)

    dic['gols'] = gols[:]
    dic['total'] = sum(gols)

    jogadores.append(dic.copy())

    opc = ' '
    while opc not in 'SN':
        opc = input('Quer continuar [S/N]? ').upper().strip()[0]
    if opc == 'N':
        break

print('-=-'*15)
print(f'\n{"Nº":<4}{"Nome":<10}{"Gols":<19}{"Total":<4}')
print('-+-'*15)
for pos, dic in enumerate(jogadores):
    print(f'{pos + 1:<4}{dic["nome"]:<10}{str(dic["gols"]):<20}{dic["total"]:<4}')
print('-+-'*15)

while True:
    num = int(input('Mostrar os dados de qual jogador (99 fim)? '))

    if num == 99:
        break
    elif num > len(jogadores):
        print('Opção Inválida!')
    else: 
        print(f'\n-> Levantamento do jogador {jogadores[num - 1]["nome"]}: \n')
        for pos, gol in enumerate(jogadores[num - 1]['gols']):
            print(f'    ==> Na partida {pos + 1}, fez {gol} gols.')
        print(f'\n-> Foi um total de {jogadores[num - 1]["total"]} gols.')
        print('-+-'*15)

print('\n >>> FINALIZADO >>> \n')
# Desafios 103

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s)')

print('-+-'*20)
nome = input('Nome do jogador: ')
gol = input('Número de gols: ')

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if nome.strip() == '':
    ficha(gol=gol)
else:
    ficha(nome, gol)

'''
==> Como eu fiz...

def testenome(nome):
    if nome.strip() != '':
        return nome
    else:
        return '<desconhecido>'

def testegol(gols):
    if gols != '' and gols.isnumeric():
        return gols
    else:
        return 0

nome = ''
gols = ''
print('-+-'*20)
nome = input('Nome do jogador: ')
gols = input('Número de gols: ')

print(f'O jogador {testenome(nome)} fez {testegol(gols)} gol(s).')
'''
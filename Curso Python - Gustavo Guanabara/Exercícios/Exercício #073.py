# Desafios 73

times = ('Corinthias', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo')

# A
print(f'\nOs 5 primeiros times são: {times[0:5]}')

# B
print(f'\nOs últimos 4 colocados são: {times[-4:]}')

# C
print(f'\nEm ordem alfabética temos: {sorted(times)}')

# D
posicao = times.index('Chapecoense')
print(f'\nO Chapecoense está na posição: {posicao + 1}')

# D => Ou 
print(f'\nO Chapecoense está na posição: {times.index("Chapecoense") + 1}')
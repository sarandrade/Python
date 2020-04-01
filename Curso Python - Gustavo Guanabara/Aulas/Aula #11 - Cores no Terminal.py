# Aula #11 - Cores no Terminal

'''
\033[ style;text;back m

- Style 
    -> 0 (nenhum)
    -> 1 (negrito)
    -> 4 (sublinhado)
    -> 7 (negativo)

- Text
    -> 30 (branca)
    -> 31 (vermelha)
    -> 32 (verde)
    -> 33 (amarelo)
    -> 34 (azul)
    -> 35 (magenta)
    -> 36 (ciano)
    -> 37 (cinza)

- Back
    -> 40 (branca)
    -> 41 (vermelha)
    -> 42 (verde)
    -> 43 (amarelo)
    -> 44 (azul)
    -> 45 (magenta)
    -> 46 (ciano)
    -> 47 (cinza)
'''
 
print('\033[0;30;41mOlá, Mundo!\033[m')

print('\033[32;43mOlá, Mundo!\033[m')

print('\033[4;33;44mOlá, Mundo!\033[m')

print('\033[1;35;43mOlá, Mundo!\033[m')

print('\033[7mOlá, Mundo!\033[m')

print('Os valores são \033[35m{}\033[m e \033[36m{}\033[m.'.format(1, 2))

print('O valor é {}{}{}.'.format('\033[34m', 11, '\033[m'))

cores = {'cor1':'\033[35m', 'cor2':'\033[36m', 'tiracor':'\033[m'}

print('O valor é {}{}{}.'.format(cores['cor1'], 11, cores['tiracor']))
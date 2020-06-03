PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

for frase in textos:
    for palavra in frase.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print(f'\nTexto possui pelo menos uma palavra proibida -> {palavra}\n')
            break

    else:
        print('Texto autorizado: ' + frase, end='\n\n')

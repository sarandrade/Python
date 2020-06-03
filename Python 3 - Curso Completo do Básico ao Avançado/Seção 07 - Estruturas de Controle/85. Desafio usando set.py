PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida'
]

for frase in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(frase.lower().split()))

    if intersecao:
        print(f'\nTexto possui palavra(s) proibida -> {intersecao}\n')
        continue

    else:
        print('Texto autorizado: ' + frase, end='\n\n')

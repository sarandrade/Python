# **kwargs -> keywords arguments

# Packing
def resultafo_f1(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


if __name__ == '__main__':
    resultafo_f1(primeiro='L. Hamilton',
                segundo='M. Verstappen',
                terceiro='S. Vettel')

# Outra alternativa

def resultafo_f1(primeiro, segundo, terceiro):
    print(f'1 -> {primeiro}')
    print(f'1 -> {segundo}')
    print(f'1 -> {terceiro}')

# Unpacking
if __name__ == '__main__':
    podium = {
        'primeiro': 'L. Hamilton',
        'segundo': 'M. Verstappen',
        'terceiro': 'S. Vettel'
        }
    resultafo_f1(**podium)

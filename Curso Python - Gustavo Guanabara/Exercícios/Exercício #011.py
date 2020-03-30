# Desafios 11

lar = float(input('Digite a largura da parede em metros: '))
alt = float(input('Digite a altura da parede em metros: '))

area = lar*alt

print('Você precisará de {} litros de tinta para pintar a parede de {} m².'.format(area/2, area))
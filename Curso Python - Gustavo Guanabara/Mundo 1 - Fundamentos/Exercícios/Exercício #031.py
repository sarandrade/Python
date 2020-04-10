# Desafios 31

km = float(input('Digite a distância da sua viagem em Km: '))

if km <= 200:
    print('O preço da sua passagem é R${:.2f}'.format(km * 0.5))
else:
    print('O preço da sua passagem é R${:.2f}'.format(km * 0.45))
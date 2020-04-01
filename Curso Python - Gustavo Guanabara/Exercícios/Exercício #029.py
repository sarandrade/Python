# Desafios 29

vel = float(input('Qual a sua velocidade em Km/h? '))

if vel > 80:
    print('Você foi multado! Sua multa custa R${:.2f}'.format((vel-80) * 7))
elif vel == 80:
    print('Cuidado!! Você está no limite de velocidade.')
else: 
    print('Abaixo do limite de velocidade.')    
# Desafios 34

sal = float(input('Digite seu salário: '))

if sal <= 1250:
    print('Se salário com o aumento será R${:.2f}.'.format(sal * 1.15))
else:
    print('Se salário com o aumento será R${:.2f}.'.format(sal * 1.1))
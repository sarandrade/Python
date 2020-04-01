# Desafios 40

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

med = (nota1 + nota2) / 2

print('Sua média foi {:.2f}.'.format(med))

if med >= 7:
    print('Parabéns!! Você foi aprovado.')
elif med >= 5:
    print('Estude mais!! Você foi para recuperação.')
else: 
    print('Não foi dessa vez, tente de novo ano que vem! Você foi reprovado.')
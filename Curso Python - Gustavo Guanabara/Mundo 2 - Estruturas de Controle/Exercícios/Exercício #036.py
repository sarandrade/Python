# Desafios 36

casa = float(input('Digite o valar da casa que deseja comprar: '))
sal = float(input('Digite o seu salário: '))
anos = float(input('Digite em quantos anos deseja pagar: '))

prest = casa / (anos * 12)

print('Para pagar uma casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f} por mês'.format(casa, anos, prest))

if prest > (sal * 0.3):
    print('Empréstimo negado.')
else: 
    print('Empréstimo aprovado!!')
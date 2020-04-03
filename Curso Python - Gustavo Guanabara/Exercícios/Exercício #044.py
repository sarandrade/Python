# Desafios 44

print('{:=^40}'.format(' Mercado '))

valor = float(input('Digite o valor do produto: '))

print('''Escolha a opção de pagamento:
[ 1 ] Dinheiro / Cheque.
[ 2 ] À vista no Cartão. 
[ 3 ] 2x no cartão.
[ 4 ] 3x ou mais no cartão.''')

opcao = int(input('Digite a sua opção: '))

if opcao == 1:
    preco = valor * 0.9
    print('O valor do produto será R${:.2f}.'.format(preco))
elif opcao == 2:
    preco = valor * 0.95
    print('O valor do produto será R${:.2f}.'.format(preco))
elif opcao == 3:
    preco = valor 
    print('O valor do produto será R${:.2f} em 2x de R${:.2f}.'.format(preco, preco / 2))
elif opcao == 4:
    parcelas = int(input('Em quantas vezes deseja pagar? '))
    preco = valor * 1.2
    print('O valor do produto será R${:.2f} em {}x de R${:.2f}.'.format(preco, parcelas, preco / parcelas))
else: 
    print('Opção inválida!')
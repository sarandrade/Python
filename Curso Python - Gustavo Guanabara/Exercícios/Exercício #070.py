# Desafios 70

print('-=-'*10)
print('  MERCADO  ')
print('-=-'*10)

total = maismil = val_barato = 0
nome_barato = ''

while True:
    nome = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    print('-'*20)
    
    total += preco

    if preco > 1000:
        maismil += 1 
    if total == preco:
        val_barato = preco 
        nome_barato = nome
    if preco < val_barato:
        val_barato = preco 
        nome_barato = nome
        
    opcao = input('Deseja continuar [S/N]? ').upper().strip()
    print('-'*20)

    if opcao == 'N':
        break
    elif opcao != 'S':
        print('Opção Inválida!! Tente de novo...')
        opcao = input('Deseja continuar [S/N]? ').upper().strip()
        print('-'*20)

print('\n-=-=-=- FIM DO PROGRAMA -=-=-=-')
print(f'Total da compra: R${total:.2f}')
print(f'Total de produtos que custam mais de R$1.000,00: {maismil}')
print(f'Produto mais barato: {nome_barato} -> R${val_barato:.2f}')
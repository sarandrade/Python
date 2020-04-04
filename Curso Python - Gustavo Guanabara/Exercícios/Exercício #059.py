# Desafios 59

opcao = menor = maior = 0

num1 = float(input('Digite o primeiro número: ')) 
num2 = float(input('Digite o segundo número: ')) 

while opcao != 5:

    print('-=-'*10)
    print('Você tem as seguintes opções: ')
    print('-=-'*10)
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    print('-=-'*10)
    opcao = int(input('Digite a opção escolhida: '))

    if opcao == 1:
        soma = num1 + num2
        print('=> {} + {} = {}'.format(num1, num2, soma))

    elif opcao == 2:
        mult = num1 * num2
        print('=> {} x {} = {}'.format(num1, num2, mult))

    elif opcao == 3:
        if num1 > num2:
            maior = num1
            menor = num2
        else:
            maior = num2
            menor = num1
        print('=> {} > {}'.format(maior, menor))
    elif opcao == 4:
        num1 = float(input('Digite o primeiro número: ')) 
        num2 = float(input('Digite o segundo número: ')) 
    elif opcao != 5:
        print('Opção Inválida... Tente novamente!')	

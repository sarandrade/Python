# Desafios 65

soma = i = maior = menor =0
opcao = 'S'

while opcao != 'N':

    if opcao == 'S':
        num = int(input('Digite um número inteiro: '))
        opcao = input('Deseja continuar [S/N]? ').upper().strip()

        soma += num
        i += 1

        if i == 1:
            maior = menor = num
        else:
            if num > maior:
                maior = num
            if num < menor:
                menor = num
    elif opcao != 'N':
        print('Opção Inválida!!')
        opcao = input('Deseja continuar [S/N]? ').upper().strip()

print('A média dos {} números digitados é {}.'.format(i, soma / i))
print('O maior número foi {}'.format(maior))
print('O menor número foi {}'.format(menor))
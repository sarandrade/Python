# Desafios 37

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converter para Hexadecimal''')

opcao = int(input('Digite a sua opção: '))

if opcao == 1:
    print('{} -> {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} -> {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} -> {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
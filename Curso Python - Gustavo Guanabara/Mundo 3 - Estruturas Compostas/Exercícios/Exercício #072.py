# Desafios 72

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    while True:
        num = int(input('Digite uma número inteiro entre 0 e 10: '))
        if 0 <= num <= 10:
            break
        print('Tente novamente...')
    print(f'O número que você digitou foi {tupla[num]}.')

    opcao = ' '
    while opcao not in 'SN':
        opcao = input('Deseja continuar [S/N]? ').upper().strip()[0]
    
    if opcao == 'N':
        break

print('Programa finalizado...')
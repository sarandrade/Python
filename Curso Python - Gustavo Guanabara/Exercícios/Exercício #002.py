# Desafio 02

dia = input('Qual o dia do seu nascimento? ')
mes = input('Qual o mês do seu nascimento? ')
ano = input('Qual o ano do seu nascimento? ')

if mes.isdigit():
    print('Você nasceu na data: ' + dia + '/' + mes + '/' + ano)
else:
    print('Você nasceu no dia {} de {} de {}'.format(dia, mes, ano))
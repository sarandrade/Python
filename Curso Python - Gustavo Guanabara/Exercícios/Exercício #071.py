# Desafios 71

print('='*20)
print('{:^20}'.format('BANCO'))
print('='*20)

valor = int(input('Qual valor deseja sacar? R$'))

while True:
    if valor >= 50:
        cedula50 = valor // 50
        print(f'=> {cedula50} cédulas de R$50,00')
        valor = valor % 50
    elif valor >= 20:
        cedula20 = valor // 20
        print(f'=> {cedula20} cédulas de R$20,00')
        valor = valor % 20
    elif valor >= 10:
        cedula10 = valor // 10
        print(f'=> {cedula10} cédulas de R$10,00')
        valor = valor % 10
    elif valor >= 1:
        cedula1 = valor // 1
        print(f'=> {cedula1} cédulas de R$1,00')
        valor = valor % 1
    else: 
        break

print('='*20)
print('Volte sempre ao BANCO! \nTenha um bom dia!!')
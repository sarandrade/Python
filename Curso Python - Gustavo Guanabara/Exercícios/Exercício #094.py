# Desafios 94

pessoa = {}
lista = []
soma = 0

while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')

    sexo = ' '
    while sexo not in 'FM':
        sexo = input('Sexo [F/M]: ').upper().strip()[0]
    pessoa['sexo'] = sexo

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    lista.append(pessoa.copy())

    opc = ' '
    while opc not in 'SN':
        opc = input('Continuar [S/N]? ').upper().strip()[0]
    if opc == 'N':
        break

print('-=-'*10)

print(f'==> O grupo tem {len(lista)} pessoas.')

media = soma / len(lista)
print(f'==> A média de idade é de {media:.2f} anos.')

print(f'==> As mulheres cadastradas foram: ', end='')
for pessoa in lista:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"]} ', end='')

print(f'\n==> Pessoas que estão acima da média: ')
for pessoa in lista:
    if pessoa['idade'] > media:
        print(f'    -> Nome = {pessoa["nome"]}; Sexo = {pessoa["sexo"]}; Idade = {pessoa["idade"]}')

print('-=-'*10)
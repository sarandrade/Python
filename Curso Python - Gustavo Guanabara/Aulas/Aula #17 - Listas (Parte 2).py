# Aula #17 - Listas (Parte 2)

pessoa = []
pessoa.append('Sara')
pessoa.append(21)

grupo = [['Mari', 2]]
grupo.append(pessoa[:]) # Faz uma cópia apenas
print(grupo)

pessoa[0] = 'Túlio'
pessoa[1] = 21

grupo.append(pessoa[:]) # Faz uma cópia apenas
print(grupo)
print(grupo[0]) # Mostra toda a primeira lista
print(grupo[0][0]) # Mostra apenas o primeiro termo da primeira lista

for lista in grupo:
    print(f'{lista[0]} tem {lista[1]} anos.')

galera = []
dados = []

for c in range(0, 3):
    dados.append(input('Nome: '))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for i in galera:
    if i[1] >= 21:
        print(f'{i[0]} é maior de idadde.')
    else: 
        print(f'{i[0]} é menor de idadde.')

# Desafios 84 -> 89
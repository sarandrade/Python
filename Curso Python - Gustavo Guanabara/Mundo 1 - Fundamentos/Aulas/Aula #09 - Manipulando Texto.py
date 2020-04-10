# Aula #09 - Manipulando Texto

frase = ' Sara Andrade Dias'

'''
Fatiamento
'''
print(frase[5])
print(frase[5:10])
print(frase[5:10:2])

'''
Análise 
'''
print(len(frase)) # Tamanho 
print(frase.count('a')) # Contagem da letra 'a' em frase
print(frase.count('a', 0, 5)) # Contagem com fatiamento
print(frase.find('Dias')) # Localiza 'Dias' em frase
print('a' in frase) # Verifica se 'a' está contido em frase

'''
Transformação
'''
print(frase.replace('Andrade', 'Araújo')) # Substitui 'Andrade' por 'Araújo'
print(frase.upper()) # Torna tudo maiúsculo
print(frase.lower()) # Torna tudo minúsculo
print(frase.capitalize()) # Torna tudo minúsculo exceto a primeira letra da frase
print(frase.title()) # Torna tudo minúsculo exceto a primeira letra de cada palavra
print(frase.strip()) # Remove espaços inúteis no início e no fim
print(frase.rstrip()) # Remove espaços inúteis no fim apenas(r -> right)
print(frase.lstrip()) # Remove espaços inúteis no início apenas (l -> left)

'''
Divisão
'''
lista = frase.split() # Dividir uma string em uma lista
print(lista) 
print(lista[0])
print(lista[0][0])

'''
Junção
'''
print('-'.join(lista))

'''
'''

print('''A PythonBrasil é o maior evento sobre linguagem de programação Python do Brasil. Feito pela comunidade para a comunidade, tem o objetivo de difundir a linguagem, promover a troca de experiências e manter a comunidade crescendo igualmente em público e impacto social.''')

# Desafios 22 -> 27
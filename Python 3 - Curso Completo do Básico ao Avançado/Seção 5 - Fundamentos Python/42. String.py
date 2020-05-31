# print(dir(str))

nome = 'Sara Andrade Dias'

print(nome[0])
print(nome[-1])
print(nome[5:])
print(nome[-4:])
print(nome[:3]) # O último índice (3) não será exibido

print(len(nome)) # Tamanho da string

print(nome.lower()) # Todas as letras minúsculas
print(nome.upper()) # Todas as letras maiúsculas

print('sara' in nome.lower())

print(nome.split()) # Quebrar a string nos espaços
print(nome.split('a')) # Quebrar a string nas letras 'a'

# nome[0] = 'P' -> Não é possível fazer essa atribuição pois a string é imutavel

numeros = '1234567890'
print(numeros[::2]) # Exibir do início ao fim pulando de 2 em 2
print(numeros[1::2]) 
print(numeros[::-1]) # Inverte a string 

# print('Marca d'água') -> Erro
print("Marca d'água")
print('Marca d\'água')

# Quebrando linha
texto = '''Texto com múltiplas
    ...linhas'''
print(texto)
print('Texto com múltiplas \n\t...linhas')

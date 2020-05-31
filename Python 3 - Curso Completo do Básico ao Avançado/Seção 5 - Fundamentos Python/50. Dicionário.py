# print(dir(dict))

# dict = {'chave':'valor'}
# dict = {'key':'value'}

pessoa = {'nome':'Sara', 'idade':21, 'idiomas':['Inglês', 'Português']}

print(len(pessoa)) # Quantidade de itens do dict

print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['idiomas'])
print(pessoa['idiomas'][0])

print(pessoa.keys()) # Retorna as chaves
print(pessoa.values()) # Retorna os valores
print(pessoa.items()) # Retorna as chaves e os valores

pessoa['idade'] = 22 # Atribui um novo valor à chave 'idade'
print(pessoa)

print(pessoa.get('idade')) # Retorna o valor da chave 'idade'
print(pessoa.get('abc', ())) # Se não encontrar a chave 'abc' retorna ()

pessoa['idiomas'].append('Alemão') # Adiciona um valor relaconado a chave 'idioma'
print(pessoa)

pessoa.pop('idade') # Remove o par indexado à chave 'idade'
print(pessoa)

pessoa.update({'idade':21, 'sexo':'F'}) # Adiciona itens
print(pessoa)

del pessoa['idiomas'] # Remove o par indexado à chave 'idiomas'
print(pessoa)

pessoa.clear() # Limpa o dict
print(pessoa)

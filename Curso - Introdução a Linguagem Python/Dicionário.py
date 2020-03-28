# Curso - Introdução a Linguagem Python

'''
dicionario = {'chave1':'valor1','chave2':'valor2'}
print(dicionario)
print(dicionario['chave1'])
'''
sara = {
    'nome': 'Sara',
    'idade': 21
}
tulio = {
    'nome': 'Túlio',
    'idade': 22
}
lista_telefonica = {'Sara':'981986290', 'Túlio':'999214114'}

print(tulio['nome'])
print(lista_telefonica['Sara'])
print(lista_telefonica)

for chave in lista_telefonica:
    print(chave+' : '+lista_telefonica[chave])

for i in lista_telefonica.items():
    print(i)    

for i in lista_telefonica.keys():
    print(i) 

for i in lista_telefonica.values():
    print(i) 
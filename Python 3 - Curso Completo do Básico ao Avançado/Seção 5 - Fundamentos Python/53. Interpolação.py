nome, idade = 'Sara', 21.5

# Versão mais antiga de interpolação
print('Nome: %s | Idade: %d' % (nome, idade))
print('Nome: %s | Idade: %.2f' % (nome, idade))
print('%r %r' % (True, False))
print('%d %d' % (True, False))

# Versão mais recomendada para Python < 3.6 de interpolação
print('Nome: {} | Idade: {}'.format(nome, idade))
print('Nome: {0} | Idade: {1}'.format(nome, idade))

# Versão disponível a partir do Python 3.6 de interpolação
print(f'Nome: {nome} | Idade: {idade} | {2 ** 8}')

from string import Template

a = Template('Nome: $n | Idade: $id')
print(a.substitute(n=nome, id=idade))

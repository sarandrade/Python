# Aula #13 - Estrutura de Repetição for

'''
for i in range(0, 10):
    comandos 
'''

for i in range(0, 5): # Não conta o número 5. Logo repete 5 vezes os comandos.
    print('{}'.format(i))
print('FIM')

for i in range(4, -1, -1): # -1 diz o que irá acontecer com o iterador
    print('{}'.format(i))

i = int(input('Início: '))
f = int(input('FIM: '))
p = int(input('Passo: '))

for c in range(i, f + 1, p):
    print(c)

s = 0
for i in range(0, 4):
    n = int(input('Digite um número: '))
    s = s + n # Ou s += n
print('Soma = {}.'.format(s))

# Desafios 46 -> 56
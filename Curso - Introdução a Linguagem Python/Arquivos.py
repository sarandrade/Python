# Curso - Introdução a Linguagem Python

'''
Funções 
- open
    a = open(nome, modo)
'''
'''
Modo
- r = somente leitura
- w = escrita (caso o arquivo já exista, ele será apagado e um novo arquivo vazio será criado)
- a = leitura e escrita (adiciona o novo conteúdo ao fim do arquivo)
'''
'''
Lendo arquivos
- read() = lê arquivo inteiro
- readline() = lê uma linha
- readlines() = lê arquivo e o armazena em uma lista
'''
arquivo = open('teste1.txt')

linhas = arquivo.readlines()
print(linhas)

for linha in linhas:
    print(linha)

arquivo = open('teste1.txt')

testo_completo = arquivo.read()
print(testo_completo)

arquivo = open('teste1.txt')

linha1 = arquivo.readline(15)
print(linha1)
linha2 = arquivo.readline()
print(linha2)
linha3 = arquivo.readline()
print(linha3)

w = open('teste2.txt', 'w')
w.write('Novo arquivo teste\n')
w.close()

w = open('teste2.txt', 'a')
w.write('Novo arquivo teste')
w.close()
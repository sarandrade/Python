# Curso - Introdução a Linguagem Python

lista1 = [1,2,3,4,5]
lista2 = ['abacaxi','balão','castanha','dado','escova']
lista3 = [100,200,300,400,500] 

for num, nome, valor in zip(lista1,lista2,lista3):
    print(num, nome, valor)
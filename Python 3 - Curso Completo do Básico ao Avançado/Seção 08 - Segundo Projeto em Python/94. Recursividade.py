def imprimir (maximo, atual):
    # Condição de parada
    if atual >= maximo:
        # A funçaõ não vai retornar nenhum tipo de valor
        return
    
    print(atual, end=' ')
    imprimir(maximo, atual + 1)


imprimir(10, 1)

'''
# Outra Alternativa 

def imprimir (maximo, atual):
    # Condição de parada
    if atual < maximo:    
        print(atual, end=' ')
        imprimir(maximo, atual + 1)


imprimir(10, 1)
'''

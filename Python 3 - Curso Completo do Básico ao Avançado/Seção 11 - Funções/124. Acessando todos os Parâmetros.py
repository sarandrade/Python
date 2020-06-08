def todos_parans(*args, **kwargs):
    print(f'args: {args}') # Tupla
    print(f'kwargs: {kwargs}') # Dicionário


if __name__ == "__main__":
    # 3 Parâmetros Posicionais
    todos_parans('a', 'b', 'c')
    # 3 Parâmetros Posicionais e 2 Parâmetros Nomeados
    todos_parans(1, 2, 3, legal=True, valor=12.99)
    # 3 Parâmetros Posicionais e 2 Parâmetros Nomeados
    todos_parans('Ana', False, [1, 2, 2], tamanho='M', fragil=False)
    # Os parâmetros posicionais ficam antes dos parâmetros nomeados 

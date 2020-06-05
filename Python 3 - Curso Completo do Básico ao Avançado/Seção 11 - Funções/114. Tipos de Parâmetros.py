'''
Funções 

-> Parâmetro posicional
    func(p1, p2, p3) = func(1, 2, 3)

-> Parâmetro nomeado
    func(p1, p2, p3) = func(1, p3=2, p2=3)

-> Parâmetro *args - Gera uma tupla
-> Parâmetro *kwargs - Gera um dicionário

'''
def tag_bloco(texto, classe='sucess'):
    return f'<div class"{classe}">{texto}</div>'


if __name__ == "__main__":
    # Testes utilizando 'assertions'
    assert tag_bloco('Incluído com sucesso!') == '<div class"sucess">Incluído com sucesso!</div>'
    assert tag_bloco('Impossível excluir!') == '<div class"sucess">Impossível excluir!</div>'
    print(tag_bloco('bloco'))

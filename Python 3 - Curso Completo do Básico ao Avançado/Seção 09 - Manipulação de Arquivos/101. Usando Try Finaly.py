try:
    arquivo = open('Pessoas.csv', encoding='utf8')
    # Lê o arquivo sob demanda, não carrega tudo na memória -> Stream

    for pessoa in arquivo:
        # strip() -> Tira os espaços em branco no começo e no fim da string
        # split(',') -> Quebra a string em ','
        print('Nome: {} | Idade: {}'.format(*pessoa.strip().split(',')))

except IndexError:
    pass

# O arquivo vai ser fechado independente de qualquer situação
finally:
    arquivo.close()
    print('Arquivo foi fechado!')

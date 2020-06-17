from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português do Brasil
setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do ano com 31 dias

# 1. (filter) - Pegar os índices dos meses com 31 dias
indice_mes = filter(lambda indice: mdays[indice] == 31, range(1, 13)) 

# 2. (map) - Transformar os índices em nome
nome_mes = map(lambda indice: month_name[indice], indice_mes)

# 3. (reduce) - Jintar tudo para imprimir
reduzido = reduce(lambda string, mes: f'{string}\n' + f'- {mes}', nome_mes, 'Meses com 31 dias:')
print(reduzido)

# Outra Alternativa

def mes_com_31(mes): return mdays[mes] == 31


def get_nome_mes(mes): return month_name[mes]


def juntar_meses(string, mes): return f'{string}\n' + f'- {mes}'


print(
    reduce(
    juntar_meses,
    map(
        get_nome_mes, 
        filter(mes_com_31, range(1, 13))
        ),
    'Meses com 31 dias:'
    )
)

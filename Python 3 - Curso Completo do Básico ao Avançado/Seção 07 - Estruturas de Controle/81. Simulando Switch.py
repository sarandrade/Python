# Simulando o Switch
def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado'
    }

    return dias.get(dia, '** Inválido **')


def get_tipo_dia(dia):
    dias = {
        1: 'Fim de Semana',
        2: 'Dia de Semana',
        3: 'Dia de Semana',
        4: 'Dia de Semana',
        5: 'Dia de Semana',
        6: 'Dia de Semana',
        7: 'Fim de Semana'
    }

    return dias.get(dia, 'Indeterminado.')

if __name__ == '__main__':
    for dia in range(8):
        print(f'{dia} -> {get_dia_semana(dia)} -> {get_tipo_dia(dia)}')

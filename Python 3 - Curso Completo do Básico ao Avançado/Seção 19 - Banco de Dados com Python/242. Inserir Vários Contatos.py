from mysql.connector.errors import ProgrammingError
from conexao import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Ana', '98455-4321'),
    ('Bia', '98765-7821'),
    ('Sara', '99665-4321'),
    ('Mari', '98765-4851'),
    ('Malu', '98765-4451'),
    ('Odra', '98745-4321'),
    ('Nusa', '99765-4451')
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'-> Foram incluídos {cursor.rowcount} registros!')
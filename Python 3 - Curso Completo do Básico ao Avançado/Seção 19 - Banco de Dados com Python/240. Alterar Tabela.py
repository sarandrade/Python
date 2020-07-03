from mysql.connector.errors import ProgrammingError
from conexao import nova_conexao

sql = 'ALTER TABLE contatos ADD COLUMN id int auto_increment PRIMARY KEY'

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql)
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
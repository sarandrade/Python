from mysql.connector.errors import ProgrammingError
from conexao import nova_conexao

sql = 'DELETE FROM contatos WHERE nome = %s'
args = ('Lucas',)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'{cursor.rowcount} registro(s) deletado(s)!')
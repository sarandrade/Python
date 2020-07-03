from conexao import nova_conexao
from mysql.connector import ProgrammingError


tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos(
        nome varchar(50),
        tel varchar(40)
    )
"""

tabela_emails = """
    CREATE TABLE emails(
        id int auto_increment PRIMARY KEY,
        dono varchar(50)
    )
"""

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(tabela_contatos)
            cursor.execute(tabela_emails)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro de Conexão: {e.msg}')
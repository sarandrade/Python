from conexao import nova_conexao
from mysql.connector import ProgrammingError


criar_tabela_grupos = """
    CREATE TABLE IF NOT EXISTS grupos (
        id int auto_increment PRIMARY KEY,
        descricao varchar(30)
    )
"""

alterar_tabela_contatos_1 = """
    ALTER TABLE contatos ADD grupo_id int
"""

alterar_tabela_contatos_2 = """
    ALTER TABLE contatos ADD FOREIGN KEY (grupo_id) REFERENCES grupos(id)
"""

try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(criar_tabela_grupos)
            cursor.execute(alterar_tabela_contatos_1)
            cursor.execute(alterar_tabela_contatos_2)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro de Conexão: {e.msg}')
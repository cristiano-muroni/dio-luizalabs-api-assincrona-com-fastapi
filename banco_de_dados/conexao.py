import sqlite3
from pathlib import Path


ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")

cursor = conexao.cursor()


def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )


def inserir_registros(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data)
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


# novos_dados = [
#     ("Jaqueline", "jaqueline@gmail.com", 5),
#     ("Wilson", "wilson@gmail.com", 6),
#     ("Rosa", "rosa@gmail.com", 7),
# ]


def atualizar_varios_registros(conexao, cursor, novos_dados):
    try:
        cursor.executemany("UPDATE clientes SET nome=?, email=? WHERE id=?;", novos_dados)
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        print(e)


def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()


def recuperar_cliente(cursor, id):
    cursor.row_factory = sqlite3.Row #trocando a factory do cursor para retornar um dicionário ao invéz de tupla 
    data = (id,)
    cursor.execute("SELECT * FROM clientes WHERE id=?;", data)
    return cursor.fetchone()

def listar_todos_clientes(cursor):   
    try:
       cursor.execute("SELECT * FROM clientes;")
       return  cursor.fetchall()
    except Exception as e:
        print(f" Erro ao listar: {e}")
          
      
        
    


# atualizar_registro(conexao, cursor, 'nome', 'nome@gmail.com')
# atualizar_varios_registros(conexao, cursor, novos_dados)
# excluir_registro(conexao, cursor, 6)

clientes = listar_todos_clientes(cursor)
for cliente in clientes:
    print(cliente)

cliente = dict(recuperar_cliente(cursor, 1))
print('----------------')
print(cliente)
print(cliente["id"], cliente["nome"], cliente["email"])
print("----------------")


resultado = cursor.execute("SELECT count(*) FROM clientes").fetchone()
print(f"Total de registros na tabela: {resultado[0]}")

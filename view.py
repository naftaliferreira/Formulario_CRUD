# importando SQLite
import sqlite3 as lite


# CRUD

# Create = Inserir / Criar

# Read = Acessar / Mostrar

# Update = Atualizar

# Delete = Excluir / Apagar

# criando conexão
con = lite.connect("dados.db")


# Função inserir informações
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)


# Função acessar informações
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            lista.append(i)
    return lista


"""
# Função para atualizar informações
lista = ['joao', '1']

with con:
    cur = con.cursor()
    query = "UPDATE formulario SET nome=? WHERE id=?"
    cur.execute(query, lista)

# Função para deletar informações
lista = [1]

with con:
    cur = con.cursor()
    query = "DELETE FROM formulario WHERE id=?"
    cur.execute(query, lista)
"""

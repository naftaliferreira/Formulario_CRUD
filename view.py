# importando SQLite
import sqlite3 as lite


# CRUD

# Create = Inserir / Criar

# Read = Acessar / Mostrar

# Update = Atualizar

# Delete = Excluir / Apagar

# criando conexão
con = lite.connect("dados.db")


lista = [
    "Joao Futi",
    "joao@mail.com",
    123456789,
    "12/19/2010",
    "Normal",
    "gostaria de consultar pessoalmente",
]
"""
# Função inserir informações
with con:
    cur = con.cursor()
    query = "INSERT INTO formulario (nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
    cur.execute(query, lista)
"""
# Função acessar informações
with con:
    cur = con.cursor()
    query = "SELECT * FROM formulario"
    cur.execute(query)
    info = cur.fetchall()
    print(info)

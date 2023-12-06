# importando SQLite
import sqlite3 as lite

# criando conexão
con = lite.connect("form.db")

# criando tabela
with con:
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE Formulario(id INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT, email TEXT, telefone TEXT,  dia_em DATE, estado TEXT, assunto TEXT)"
    )

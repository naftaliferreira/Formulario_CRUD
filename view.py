# importações
import sys
import sqlite3 as lite
from datetime import datetime


# criando conexão
con = lite.connect("form.db")


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


# Função para atualizar informações


def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=? email=? telefone=? dia_em=? estado=? assunto=? WHERE id=?"
        cur.execute(query, i)


# Função para deletar informações
lista = [1]
"""
with con:
    cur = con.cursor()
    query = "DELETE FROM formulario WHERE id=?"
    cur.execute(query, lista)

"""

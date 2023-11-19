# importando o tkinter
from tkinter import *

################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # sky blue


################### criando janela

janela = Tk()
janela.title("")
janela.geometry("1043x453")
janela.configure(bg=co9)
janela.resizable(
    width=False, height=False
)  # impede que a janela tenha o seu tamanho reajustado com o mouse

################### dividindo a janela

frame_cima = Frame(janela, width=310, height=50, bg=co2, relief="flat")
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direito = Frame(janela, width=588, height=403, bg=co1, relief="flat")
frame_direito.grid(row=0, column=1, rowspan=2, padx=1, pady=1, sticky=NSEW)

################### label cima
app_nome = Label(
    frame_cima,
    text="Formulário de consultoria",
    anchor=NW,
    font=("Ivy 13 bold"),
    bg=co2,
    fg=co1,
    relief="flat",
)
app_nome.place(x=10, y=20)

################### Configurando frame baixo
# Nome
l_nome = Label(
    frame_baixo,
    text="Nome *",
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co1,
    fg=co4,
    relief="flat",
)
l_nome.place(x=10, y=10)

e_name = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_name.place(x=15, y=40)

# email
l_email = Label(
    frame_baixo,
    text="email *",
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co1,
    fg=co4,
    relief="flat",
)
l_email.place(x=10, y=70)

e_email = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_email.place(x=15, y=100)

# telefone
l_telefone = Label(
    frame_baixo,
    text="telefone *",
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co1,
    fg=co4,
    relief="flat",
)
l_telefone.place(x=10, y=130)

e_telefone = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_telefone.place(x=15, y=160)
"""
# Data da consulta
l_datacon = Label(
    frame_baixo,
    text="Data da consulta *",
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co1,
    fg=co4,
    relief="flat",
)
l_datacon.place(x=10, y=10)

e_datacon = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_datacon.place(x=15, y=40)

# Estado
l_estado = Label(
    frame_baixo,
    text="Estado *",
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co1,
    fg=co4,
    relief="flat",
)
l_estado.place(x=10, y=10)

e_estado = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_estado.place(x=15, y=40)

# Sobre
l_sobre = Label(
    frame_baixo,
    text="Consulta sobre *",
    anchor=NW,
    font=("Ivy 10 bold"),
    bg=co1,
    fg=co4,
    relief="flat",
)
l_sobre.place(x=10, y=10)

e_sobre = Entry(frame_baixo, width=45, justify="left", relief="solid")
e_sobre.place(x=15, y=40)
"""

janela.mainloop()

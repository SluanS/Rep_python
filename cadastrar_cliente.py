import sqlite3
import tkinter as tk
from tkinter import ttk

conn = sqlite3.connect("c:\dados\clientes.db")
cursor = conn.cursor()
cursor.execute("create table if not exists cadastros(id int, nome varchar(30), telefone varchar(30), email varchar(30))")

def limpeza(): #função responsável por limpar a tabela e as caixas de entrada após cada novo submit
    valores = tree.get_children()#Busca o id de todas as dependências da TREEVIEW principal e armazena em uma tupla
    for c in valores: 
        tree.delete(c) #deleta todos os dados citados pelo laço

    nome_entrada.delete(first=0,last=tk.END) #Deleta todas as informações contidas dentro das caixas de entrada da tela root
    telefone_entrada.delete(first=0,last=tk.END)
    email_entrada.delete(first=0,last=tk.END)

# Insere um novo herói no banco; garante IDs únicos simulando autoincremento manual
def adicionar_clientes():
    cursor.execute("SELECT * FROM cadastros ORDER BY id DESC LIMIT 1") 
    ultimo_id = cursor.fetchall() #recolhe as informações obtidas pela querry do select
    n = nome_entrada.get() #aloca em um objeto os dados contidos nas caixas de entrada
    e = telefone_entrada.get()
    l = email_entrada.get()
    if len(ultimo_id) > 0: #Verifica se já foi inserido um primeiro registro no banco de dados
        cursor.execute(f"insert into cadastros values({ultimo_id[0][0] + 1},'{n}','{e}','{l}')")
    else:
        cursor.execute(f"Insert into cadastros values({1},'{n}','{e}','{l}')")
    conn.commit()
    limpeza() #Chama a função que limpará as caixas de entrada e o Treeview

def mostrar_clientes(): #função responsaável por inserir os valores na Treeview e exibi-los
    cursor.execute("select * from cadastros") #Consulta todos os dados da tabela hero
    resultado = cursor.fetchall() #Armazena esses dados em um objeto

    for c in resultado: #insere os dados obtidos dentro do Treeview
        tree.insert('',index="end",values=(c[1],c[2],c[3]))

root = tk.Tk()  #Criação e confirguração da tela principal
root.geometry("1000x600")
root.title("Cadastros de Cliente") 
tk.Label(root,text="Insira os dados para registro:").grid(row=0, column=0)

#Criação de caixas de entrada e seus labels
tk.Label(root,text="Nome").grid(column=0,row=1,sticky=tk.E) #Cria o texto que servirá como guia
nome_entrada = tk.Entry(root) #cria a entrada para inserção de dados
nome_entrada.grid(column=1,row=1,sticky="nsew") #organização do widget dentro da tela principal(root)

tk.Label(root,text="Telefone").grid(column=0,row=2,sticky=tk.E)
telefone_entrada = tk.Entry(root)
telefone_entrada.grid(column=1,row=2,sticky="nsew")

tk.Label(root,text="Email").grid(column=0,row=3,sticky=tk.E)
email_entrada = tk.Entry(root)
email_entrada.grid(column=1,row=3,sticky="nsew")

#Criação de botão responsável responsável por adicionar os registros ao banco de dados, possui a função "adicionar" atrelada a ele
sub = ttk.Button(root,text="Submit", command=adicionar_clientes)
sub.grid(column=3,row=4)

#Botão responsável por tornar os registros visiveis no Treeview, possui a função de 'listagem' atrelada
see = ttk.Button(root,text="Ver lista", command=mostrar_clientes)
see.grid(column=3,row=5)


#Cria a Treeview e configura ela como uma Treeview de dados tabulares
tree = ttk.Treeview(root, show="headings", columns=("Nome", "Telefone", "Email"))
tree.heading("Nome",text="Nome")
tree.heading("Telefone",text="Telefone")
tree.heading("Email", text="Email")
tree.grid(row=6,column=2)
#
root.mainloop() 
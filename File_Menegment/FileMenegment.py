import tkinter as tk
from tkinter import ttk
import os


caminho = os.getcwd()
caminho = caminho.split(sep="\\")
dados_no_diretorio = os.listdir()

root = tk.Tk()
root.geometry("800x700")
root.title("Navigating with Treeview")
tree = ttk.Treeview(root,show="tree",height=20,)
tree.insert(parent="",index=0,text=caminho[-1])
for c in range(len(dados_no_diretorio)):
    tree.insert(parent="I001",index=c,text=dados_no_diretorio[c])
tree.pack()

root.mainloop()
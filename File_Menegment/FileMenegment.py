import tkinter as tk
from tkinter import ttk
import os

os.chdir("C:/Users/atlua/OneDrive/Área de Trabalho")
caminho = os.getcwd()
caminho = caminho.split(sep="\\")
dados_no_diretorio = os.listdir()

root = tk.Tk()
root.geometry("800x700")
root.title("Navigating with Treeview")
imagem = tk.PhotoImage(file="C:/VS_code_geral/rep/File_Menegment/imgs/file_icon.png")
imagem2 = tk.PhotoImage(file="C:/VS_code_geral/rep/File_Menegment/imgs/directory_icon.png")
tree = ttk.Treeview(root,show="tree",height=20,)
tree.insert(parent="",index=0,text=caminho[-1])
for c in range(len(dados_no_diretorio)):
    current_path = str("\\".join(caminho)) + "\\" + dados_no_diretorio[c]
    print(current_path)
    tree.insert(parent="I001",index=c,text=dados_no_diretorio[c],image=imagem if os.path.isfile(current_path) else imagem2)

tree.pack()
root.mainloop()
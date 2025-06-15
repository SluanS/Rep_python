import os
from os import path
import tkinter as tk
from tkinter import filedialog,ttk
import shutil
root = tk.Tk()
root.geometry("700x500")
root.title("Search file")
root.columnconfigure(index=0,weight=2)
caminho = ""
frame1 = tk.Frame(root)
frame1.columnconfigure(index=0,weight=20)
frame1.pack(expand=True,fill="both")

#Imagem
file_image =tk.PhotoImage(file=os.getcwd()+"\\file_Menegment\\imgs\\file_icon.png")
folder_image = tk.PhotoImage(file=os.getcwd()+"\\file_Menegment\\imgs\\directory_icon.png")


def exibir_diretorio():
    global caminho
    itens = os.listdir(caminho)
   
    for i in itens:
        #print(f"caminho atual: {caminho}/{i}")
        tree.insert(parent="",index="end",text=i,image=file_image if path.isfile(f"{caminho}/{i}") else folder_image)


def search():
    global caminho
    if tree.get_children() != "":
        for c in tree.get_children():
            tree.delete(c)
    caminho = filedialog.askdirectory()
    #os.chdir(caminho)
    exibir_diretorio()
    print(tree.get_children())
    return caminho


def organizar_arquivos():
    global caminho
    try:
        files_extension_folders = ("pdf","png","jpeg")
        for b in files_extension_folders:
            if not path.exists(caminho+"/"+b+"_folder"):
                            os.mkdir(caminho+f"/{b}_folder")
        for c in os.listdir(caminho):
            print(caminho+"/"+c)
            if path.isfile(caminho+"/"+c):
                descobrir_exntensao = path.splitext(c)[1][1:]
                if descobrir_exntensao.lower() in files_extension_folders:
                    print(descobrir_exntensao," descobrir extensão")
                    shutil.move(src=caminho+"/"+c,dst=caminho+"/"+descobrir_exntensao+"_folder")
            
        #atualiza Treeview ao apertar o botão 
        if tree.get_children() != "":
            for c in tree.get_children():
                tree.delete(c)
            exibir_diretorio()
    except:
         print("Nenhum caminho especificado")

           


consult_button = ttk.Button(frame1,text="Search",command=search)
consult_button.pack()


organize_button = ttk.Button(frame1,text="Organize",command=organizar_arquivos)
organize_button.pack(side="right")


#treeview
tree = ttk.Treeview(frame1,show="tree",height=20)
tree.columnconfigure(index=0,weight=40)
tree.pack(expand=True,fill="both")

root.mainloop()


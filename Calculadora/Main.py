
import tkinter as tk
from tkinter import ttk
from abc import abstractmethod,ABC

root = tk.Tk()
root.geometry("448x550")
root.title("Minicalculadora")
inseridos=tk.Label(root,text="0")
inseridos.config(font=("Arial",30))
inseridos.grid(column=0,row=0)


"""n1 = ttk.Entry(root,width=10)
n2 = ttk.Entry(root,width=10)
n1.grid(column=0,row=1)
n2.grid(column=1,row=1)"""

"""def limpar():
    n1.delete(first=0,last=tk.END)
    n2.delete(first=0,last=tk.END)"""
componente = ""
def exibicao():
    componente1 = ""
    componente2 = ""
def somar():
    num1 = n1.get()
    num2 = n2.get()
    resultado = int(num1) + int(num2)
    tk.Label(root,text=resultado,bg="bisque3").grid(column=4,row=1)
    limpar()
def subtrair():
    num1 = n1.get()
    num2 = n2.get()
    resultado = n1 - n2 
def multiplicar():
    num1 = n1.get()
    num2 = n2.get()
    resultado = num1 * num2


btn_plus = tk.Button(root,width=10,height=6,text="+",bg="springgreen3",command=somar)
btn_minum = tk.Button(root,width=10,height=6,text="-",bg="springgreen3",command=subtrair)
btn_mult = tk.Button(root,width=10,height=6,text="X",bg="springgreen3",command=multiplicar)
btn_div = tk.Button(root,width=10,height=6,text="/",bg="springgreen3")
btn_equa = tk.Button(root,width=10,height=6,text="=",bg="springgreen3")
botoes = (btn_plus,btn_minum,btn_mult,btn_div,btn_equa)
for i,v in enumerate(botoes):
    v.grid(row=2+i,column=4)

b0 = tk.Button(root,width=10,height=6,text='0',bg="PaleGreen2", lambda: componente += 0).grid(row=5,column=1)
b1 = tk.Button(root,width=10,height=6,text='1',bg="PaleGreen2").grid(row=4,column=0)
b2 = tk.Button(root,width=10,height=6,text='2',bg="PaleGreen2").grid(row=4,column=1)
b3 = tk.Button(root,width=10,height=6,text='3',bg="PaleGreen2").grid(row=4,column=2)
b4 = tk.Button(root,width=10,height=6,text='4',bg="PaleGreen2").grid(row=3,column=0)
b5 = tk.Button(root,width=10,height=6,text='5',bg="PaleGreen2").grid(row=3,column=1)
b6 = tk.Button(root,width=10,height=6,text='6',bg="PaleGreen2").grid(row=3,column=2)
b7 = tk.Button(root,width=10,height=6,text='7',bg="PaleGreen2").grid(row=2,column=0)
b8 = tk.Button(root,width=10,height=6,text='8',bg="PaleGreen2").grid(row=2,column=1)
b9 = tk.Button(root,width=10,height=6,text='9',bg="PaleGreen2").grid(row=2,column=2)

n_botoes = (b0,b1,b2,b3,b4,b5,b6,b7,b8,b9)


root.mainloop()

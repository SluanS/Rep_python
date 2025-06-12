#importando o módulo tkinter para criar a interface (gui)
import tkinter as tk

#função que será chamada quando o usuário clicar em um botão da calculadora
def click(event):
    #captura o texto do botão que foi clicado
    text = event.widget.cget("text")

    #verifica se o botão clicado foi o "=" (para calcular o resultado)
    if text == "=":
        try:
            #avalia a expressão contida na tela (usando eval)
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            #caso haja erro na expressão (Ex: divisao por zero), exibe "Erro" na tela
            screen.set("Erro")

    #Se o botão clicado foi "c", limpa a tela da calculadora
    elif text == "C":
        screen.set("Erro")
    
    # Caso contrário (para qualquer outro botão), adiciona o texto do botão á expressão na tela
    else:
        screen.set(screen.get() + text)
#Configurção da janela principal da calculadora
root = tk.Tk()
root.title("Calculadora - PyCPhone")
root.geometry("350x500")
root.config(bg="#F0F0F0")

#Variável para armazenar o texto que será exibido na tela da calculadora
screen = tk.StringVar()

#Caixa de entrada onde as expressões e resultados serão exibidos
entry = tk.Entry(root, textvariable=screen, font="Arial 24", bd=10, insertwidth=2,width=14,justify="right")
#confirgura a aparencia da caixa de entrada (fonte, borda, alinhamento á direita)
entry.pack(fill="both",ipadx=8,padx=10,pady=20)

#lista botões da calculadora
buttons = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["C","0","=","+"]
    ]
# FUnção para criar os botões com estilo especifoc
def create_button(frame,text,color="#FFFFFF",bg="#C0C0C0"):
    button = tk.Button(frame,text=text, font="Arial 20", padx=20,pady=20,bg=bg,fg=color,borderwidth=0)
    button.pack(side="left",expand=True,fill="both",padx=5,pady=5)
    button.bind("<Button-1>",click)
    return button

#função para criar os botões na interface
for row in buttons:
    #criar um frame (linha) para organizar os botões da calculadora
    frame = tk.Frame(root,bg="#F0F0F0")
    frame.pack(expand=True,fill="both")
    # Para cada botão na linha, cria o botão com as cores e comportamentos apropriadas
    for button_text in row:
        if button_text in ["+","-","*","/","="]:
            #Botões de operação (+,-,*,/,=) tem cor laranja
            create_button(frame, button_text, color="#FFFFFF", bg="#FFA500")
        elif button_text == "C":
            #O botão limpar ("C") é vermelho
            create_button(frame, button_text,color="#FFFFFF", bg="#FF6347")
        else:
            create_button(frame,button_text)

root.mainloop()
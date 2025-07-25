import pyautogui
import time
import subprocess

def abrir_bloconotas():
    subprocess.Popen(["notepad.exe"])
    time.sleep(1.5)

def escrever_texto():
    texto = "Ola, isso e um teste de performance\n" * 10
    pyautogui.write(texto,interval=0.08)

def salvar_arquivo():
    pyautogui.hotkey("ctrl", "s")
    time.sleep(0.5)
    pyautogui.write("arquivo_teste.txt", interval=0.6)
    pyautogui.press("enter")

def fechar_bloconotas():
    time.sleep(1)
    pyautogui.hotkey("alt","f4")
def automacao_completa():
    abrir_bloconotas()
    escrever_texto()
    salvar_arquivo()
    fechar_bloconotas()

if __name__ == "__main__":
    import cProfile
    cProfile.run("automacao_completa()")
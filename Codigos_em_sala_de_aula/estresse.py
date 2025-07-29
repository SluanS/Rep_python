import sys #Executar


from PyQt5.QtWidgets import (
    QApplication, #Aplicação princical
    QWidget,# Janela basica
    QVBoxLayout, # layout que organiza os elementos de forma virtual
    QPushButton, # Botão clicavel
    QLabel, # rotulo do textp
    QLineEdit, # campo de entrada de texto
    QSpinBox, # Campo númerico
    QProgressBar # barra de progresso
)
from PyQt5.QtCore import Qt
#Classe que representa a janela
class TesteEstresse(QWidget):
    #Construtor da classe Qwidget (janela)
    def __init__(self):
        super().__init__()
        # Nome da janela
        self.setWindowTitle("Teste de Estresse")
        # Tamanho da janela (windows) em pixels
        self.setFixedSize(400, 300)
        # Criamos um campo vertical para os componentes
        layout = QVBoxLayout()
        # Criamos um campo de texto
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Url de teste")
        # Adicioa na tela os elementos criados
        layout.addWidget(QLabel("URL:"))
        layout.addWidget(self.url_input)

        self.qtd_spin = QSpinBox()
        self.qtd_spin.setMinimum(1)
        self.qtd_spin.setValue(50)
        layout.addWidget(QLabel("Nº de requisições: "))
        layout.addWidget(self.qtd_spin)

        self.btn = QPushButton("Iniciar o teste!")
        layout.addWidget(self.btn)

        self.progress = QProgressBar()
        layout.addWidget(self.progress)

        self.result = QLabel("Resultado dos testes")
        layout.addWidget(self.result)

        self.setLayout(layout)

if __name__ == "__main__":
    #Criamos a instância da aplicação - Roda por script
    app = QApplication(sys.argv)

    # Cria a janela conforme a classe que criamos
    janela = TesteEstresse()

    #Mostra a janela
    janela.show()

    # Loop da interface e parar a aplicação
    sys.exit(app.exec_())
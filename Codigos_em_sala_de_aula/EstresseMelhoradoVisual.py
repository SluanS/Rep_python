# Link para usar: https://jsonplaceholder.typicode.com

import sys
import requests
import threading
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QSpinBox, QProgressBar, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette, QFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class AplicativoTesteEstresse(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.resultado = []
        self.contagem_sucesso = 0
        self.contagem_erro = 0
        self.total_requisicoes = 0
        self.tempos_requisicoes = []

    def init_ui(self):
        self.setWindowTitle("Teste de Estresse")
        self.setFixedSize(500, 400)
        layout = QVBoxLayout()

        font = QFont("Arial", 10)
        self.setFont(font)

        palette = self.palette()
        palette.setColor(QPalette.Background, QColor(240, 240, 240))
        self.setPalette(palette)

        self.label_url = QLabel("Digite a URL para o teste de estresse:")
        self.label_url.setStyleSheet("font-weight: bold; color: #333;")
        layout.addWidget(self.label_url)

        self.entry_url = QLineEdit(self)
        self.entry_url.setPlaceholderText("Ex: https://www.exemplo.com")
        self.entry_url.setStyleSheet("background-color: white; padding: 5px; border-radius: 5px;")
        layout.addWidget(self.entry_url)

        self.label_requisicoes = QLabel("Número de requisições:")
        self.label_requisicoes.setStyleSheet("font-weight: bold; color: #333;")
        layout.addWidget(self.label_requisicoes)

        self.spin_requisicoes = QSpinBox(self)
        self.spin_requisicoes.setValue(200)
        self.spin_requisicoes.setMinimum(1)
        self.spin_requisicoes.setMaximum(1000)
        self.spin_requisicoes.setStyleSheet("background-color: white; padding: 5px; border-radius: 5px;")
        layout.addWidget(self.spin_requisicoes)

        self.button_iniciar = QPushButton("Iniciar Teste de Estresse", self)
        self.button_iniciar.setStyleSheet("background-color: #28a745; color: white; border-radius: 5px; padding: 10px; font-size: 14px;")
        self.button_iniciar.setCursor(Qt.PointingHandCursor)
        self.button_iniciar.clicked.connect(self.iniciar_teste)
        layout.addWidget(self.button_iniciar)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setStyleSheet("QProgressBar {background-color: #f0f0f0; border-radius: 5px; color: #28a745;}")
        layout.addWidget(self.progress_bar)

        self.label_resultado = QLabel("", self)
        self.label_resultado.setStyleSheet("font-weight: bold; color: #333;")
        layout.addWidget(self.label_resultado)

        self.setLayout(layout)

    def enviar_requisicoes(self, url, numero_requisicoes):
        self.resultado = []
        self.contagem_sucesso = 0
        self.contagem_erro = 0
        self.tempos_requisicoes = []

        def fazer_requisicao():
            try:
                inicio = time.time()
                resposta = requests.get(url)
                tempo_resposta = time.time() - inicio
                self.contagem_sucesso += 1
                self.tempos_requisicoes.append(tempo_resposta)
                self.resultado.append(f"Status: {resposta.status_code}, Tempo: {tempo_resposta:.4f} segundos")
            except Exception as e:
                self.contagem_erro += 1
                self.resultado.append(f"Erro: {e}")

            self.total_requisicoes += 1
            self.atualizar_barra_progresso()

        threads = []
        for _ in range(numero_requisicoes):
            t = threading.Thread(target=fazer_requisicao)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        self.mostrar_resultados()
        self.gerar_relatorio_pdf(numero_requisicoes)

    def atualizar_barra_progresso(self):
        progresso = int((self.total_requisicoes / self.spin_requisicoes.value()) * 100)
        self.progress_bar.setValue(progresso)

    def mostrar_resultados(self):
        media_tempo = sum(self.tempos_requisicoes) / len(self.tempos_requisicoes) if self.tempos_requisicoes else 0
        self.label_resultado.setText(
            f"Total de requisições: {self.total_requisicoes}\n"
            f"Sucesso: {self.contagem_sucesso}\n"
            f"Erros: {self.contagem_erro}\n"
            f"Tempo Médio de Resposta: {media_tempo:.4f} segundos"
        )
        self.progress_bar.setValue(100)

    def gerar_relatorio_pdf(self, numero_requisicoes):
        arquivo_pdf = "relatorio_teste_estresse.pdf"
        c = canvas.Canvas(arquivo_pdf, pagesize=letter)
        c.setFont("Helvetica", 12)

        c.drawString(100, 750, f"Relatório de Teste de Estresse")
        c.drawString(100, 730, f"Total de Requisições: {self.total_requisicoes}")
        c.drawString(100, 710, f"Sucesso: {self.contagem_sucesso}")
        c.drawString(100, 690, f"Erros: {self.contagem_erro}")
        c.drawString(100, 670, f"Tempo Médio de Resposta: {sum(self.tempos_requisicoes)/len(self.tempos_requisicoes):.4f} segundos")

        posicao_y = 650
        for linha in self.resultado:
            c.drawString(100, posicao_y, linha[:100])
            posicao_y -= 15
            if posicao_y < 100:
                c.showPage()
                posicao_y = 750

        c.save()
        print(f"Relatório PDF gerado: {arquivo_pdf}")

    def iniciar_teste(self):
        url = self.entry_url.text()
        numero_requisicoes = self.spin_requisicoes.value()

        if not url:
            QMessageBox.critical(self, "Erro", "Por favor, insira uma URL válida.")
            return

        self.button_iniciar.setEnabled(False)
        self.progress_bar.setValue(0)
        self.total_requisicoes = 0

        threading.Thread(target=self.enviar_requisicoes, args=(url, numero_requisicoes)).start()
        self.button_iniciar.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = AplicativoTesteEstresse()
    janela.show()
    sys.exit(app.exec_())

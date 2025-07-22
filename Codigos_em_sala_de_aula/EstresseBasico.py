import sys
import requests
import threading
import time

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QLabel, QLineEdit, QSpinBox, QProgressBar, QMessageBox
)
from PyQt5.QtCore import Qt

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class TesteEstresse(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Teste de Estresse")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("URL do teste")
        layout.addWidget(QLabel("URL:"))
        layout.addWidget(self.url_input)

        self.qtd_spin = QSpinBox()
        self.qtd_spin.setMinimum(1)
        self.qtd_spin.setValue(50)
        layout.addWidget(QLabel("Nº de requisições:"))
        layout.addWidget(self.qtd_spin)

        self.btn = QPushButton("Iniciar Teste")
        self.btn.clicked.connect(self.iniciar)
        layout.addWidget(self.btn)

        self.progress = QProgressBar()
        layout.addWidget(self.progress)

        self.result = QLabel()
        layout.addWidget(self.result)

        self.setLayout(layout)

    def requisitar(self, url, qtd):
        self.sucesso = 0
        self.erro = 0
        self.tempos = []
        self.total = 0
        logs = []

        def req():
            try:
                inicio = time.time()
                r = requests.get(url)
                tempo = time.time() - inicio

                self.sucesso += 1
                self.tempos.append(tempo)
                logs.append(f"Status: {r.status_code}, Tempo: {tempo:.3f}s")
            except Exception as e:
                self.erro += 1
                logs.append(f"Erro: {e}")

            self.total += 1
            self.progress.setValue(int((self.total / qtd) * 100))

        threads = [threading.Thread(target=req) for _ in range(qtd)]

        for t in threads:
            t.start()
        for t in threads:
            t.join()

        if self.tempos:
            media = sum(self.tempos) / len(self.tempos)
            self.result.setText(f"Sucesso: {self.sucesso} | Erros: {self.erro}\nMédia: {media:.3f}s")
        else:
            self.result.setText("Erro em todas as requisições")

        self.gerar_pdf(logs)

    def gerar_pdf(self, logs):
        c = canvas.Canvas("relatorio_teste_estresse.pdf", pagesize=letter)
        c.setFont("Helvetica", 12)

        c.drawString(100, 750, "Relatório Teste de Estresse")
        c.drawString(100, 730, f"Sucesso: {self.sucesso}")
        c.drawString(100, 710, f"Erros: {self.erro}")

        if self.tempos:
            media = sum(self.tempos) / len(self.tempos)
            c.drawString(100, 690, f"Média: {media:.3f}s")

        y = 670
        for log in logs:
            c.drawString(100, y, log[:100])
            y -= 15
            if y < 100:
                c.showPage()
                y = 750

        c.save()

    def iniciar(self):
        url = self.url_input.text()
        qtd = self.qtd_spin.value()

        if not url:
            QMessageBox.critical(self, "Erro", "Informe a URL!")
            return

        self.btn.setEnabled(False)
        self.progress.setValue(0)

        def executar():
            self.requisitar(url, qtd)
            self.btn.setEnabled(True)

        threading.Thread(target=executar).start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = TesteEstresse()
    janela.show()
    sys.exit(app.exec_())

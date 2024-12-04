import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap

class Janela(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(30, 30, 1400, 800)
        self.setWindowTitle("Caixa da Loja")

        # Coluna de cima (criado como QWidget)
        self.label_coluna_cima = QWidget()  
        self.label_coluna_cima.setStyleSheet("background-color: #ff0000")
        
        # Layout horizontal para a coluna de cima
        self.h_layout_cima = QHBoxLayout(self.label_coluna_cima)

        # Logo layout de cima 
        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap("C:/Users/gabriel.landrade2/Documents/JanelaCaixa/.venv/mansao.jpg"))
        self.h_layout_cima.addWidget(self.logo_label)

        # Informações do cliente
        self.informacoes_label = QLabel("**CLIENTE A VISTA <br> Dependente: ** Não informado **")
        self.informacoes_edit = QLineEdit()
        self.h_layout_cima.addWidget(self.informacoes_label)
        self.h_layout_cima.addWidget(self.informacoes_edit)

        self.esc_label = QLabel("ESC - Cancelar")
        self.esc_edit = QLineEdit()
        self.h_layout_cima.addWidget(self.esc_label)
        self.h_layout_cima.addWidget(self.esc_edit)

        # Coluna esquerda (criado como QWidget)
        self.label_coluna_esquerda = QWidget()
        self.label_coluna_esquerda.setStyleSheet("background-color: #0800ff")
        
        # Layout vertical da esquerda
        self.v_layout_esquerda = QVBoxLayout(self.label_coluna_esquerda)
        
        # Formas de pagamento
        self.formas_label = QLabel("Formas de pagamento")
        self.formas_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.formas_label)
        self.v_layout_esquerda.addWidget(self.formas_edit)

        # Dinheiro
        self.dinheiro_label = QLabel("Dinheiro")
        self.dinheiro_edit = QLineEdit()
        self.v_layout_esquerda.addWidget(self.dinheiro_label)
        self.v_layout_esquerda.addWidget(self.dinheiro_edit)

        # Coluna direita (criado como QWidget)
        self.label_coluna_direita = QWidget()
        self.label_coluna_direita.setStyleSheet("background-color: #bf04b3")
        
        # Layout vertical da direita
        self.v_layout_direita = QVBoxLayout(self.label_coluna_direita)

        # Restante
        self.restante_label = QLabel("Restante")
        self.restante_edit = QLineEdit()
        self.v_layout_direita.addWidget(self.restante_label)
        self.v_layout_direita.addWidget(self.restante_edit)

        # Layout vertical principal para as colunas
        self.v_layout = QVBoxLayout(self)

        # Adiciona as colunas ao layout principal
        self.v_layout.addWidget(self.label_coluna_cima)  # Adicionando a coluna de cima
        self.v_layout.addWidget(self.label_coluna_esquerda)  # Adicionando a coluna esquerda
        self.v_layout.addWidget(self.label_coluna_direita)  # Adicionando a coluna direita

# Criação do aplicativo e execução
app = QApplication(sys.argv)
cx = Janela()
cx.show()
app.exec_()

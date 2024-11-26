import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QVBoxLayout,QPushButton,QHBoxLayout,QTableView

class Caixa(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(30,30,1400,800)
        self.setWindowTitle("Caixa da Loja")
        
        #Coluna esquerda
        self.label_coluna_esquerda = QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#0c0}")

        #coluna direita
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#600}")

        
        
        #Cria o layout horizontal para as colunas
        self.h_layout = QHBoxLayout()

        #add coluna esquerda e direita
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)
        
        #add layout a tela
        self.setLayout(self.h_layout)

app = QApplication(sys.argv)
cx = Caixa()
cx.show()
app.exec_()

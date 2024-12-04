import sys
from pathlib import Path
# importar os componentes para a
# construção da janela
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,QTableWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap


class Janela(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(10,30,1000,700)
        self.setWindowTitle("Janela Gestão")

        self.label_azul = QLabel()
        self.label_azul.setStyleSheet("QLabel{background-color:blue}")
        self.label_azul.setFixedHeight(50)

        self.label_branca = QLabel()
        self.label_branca.setStyleSheet("QLabel{background-color:white}")

         #logo layout de cima 
        self.logo_label = QLabel ()
        self.logo_label.setPixmap(QPixmap("C:/Users/gabriel.landrade2/Documents/JanelaCaixa/.venv/mansao.jpg"))
        
        
        
        # Layout Horizontal que ficará dentro
        # da label branca
        self.h_lay_dentro_branca = QHBoxLayout()
        
        # Criação da label que representa a coluna da 
        # esquerda. Ela será inserida no layout 
        # horizontal criado acima
        self.label_col_esquerda = QLabel()
        self.label_col_esquerda.setStyleSheet("QLabel{background-color:green}")
        self.h_lay_dentro_branca.addWidget(self.label_col_esquerda)

        # Criação da label que representa a coluna da direita
        #  Ela será inserida no layout horizontal criado acima
        self.label_col_direita = QLabel()
        self.label_col_direita.setStyleSheet("QLabel{background-color:magenta}")
        self.h_lay_dentro_branca.addWidget(self.label_col_direita)

        # adicionar o layout horizontal branca na label branca
        # que está abaixo
        self.label_branca.setLayout(self.h_lay_dentro_branca)
    



        self.v_lay_global = QVBoxLayout()
        self.v_lay_global.addWidget(self.label_azul)
        self.v_lay_global.addWidget(self.label_branca)
        self.setLayout(self.v_lay_global)

        self.label_azul.addWidget(self.logo_label)

app = QApplication(sys.argv)
tela = Janela()
tela.show()
app.exec_()
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QVBoxLayout,QPushButton,QHBoxLayout,QTableView,QBoxLayout,QTableWidget 
from PyQt5.QtGui import QPixmap

class janela(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(30,30,1400,800)
        self.setWindowTitle("Caixa da Loja")

        #coluna de cima 
        self.label_coluna_cima = QLabel()
        self.label_coluna_cima.setStyleSheet("QLabel{background-color:#ff0000}")
        self.label_coluna_cima.setFixedHeight(50)
        
         
        #Coluna esquerda
        self.label_coluna_embaixo = QLabel()
        self.label_coluna_embaixo.setStyleSheet("QLabel{background-color:#0800ff}")
        

        #coluna direita
        #self.label_coluna_direita = QLabel()
        #self.label_coluna_direita.setStyleSheet("QLabel{background-color:#bf04b3}")
        
        
        
        
        #layout horizontal de cima
        self.v_layout = QVBoxLayout()

        #logo layout de cima 
        self.logo_label = QLabel ()
        self.logo_label.setPixmap(QPixmap("C:/Users/gabriel.landrade2/Documents/JanelaCaixa/.venv/mansao.jpg"))

        #add a imagem
        self.label_coluna_cima.addWidget(self.logo_label)

        self.informacoes_label = QLabel("**CLIENTE A VISTA <br> Dependente: ** Não informado **")
        self.informacoes_edit = QLineEdit()
        #self.v_layout.addWidget(self.informacoes_label)
        #self.v_layout.addWidget(self.informacoes_edit)

        self.esc_label = QLabel("ESC - Cancelar")
        self.esc_edit = QLineEdit()
        #self.v_layout.addWidget(self.esc_label)
        #self.v_layout.addWidget(self.esc_edit)

        

        
        #layout vertical da esquerda
        self.v_layout_esquerda = QHBoxLayout()

        #labels da esquerda

        self.formas_label = QLabel ("Formas de pagamento")
        self.formas_edit = QLineEdit()
        #self.v_layout_esquerda.addWidget(self.formas_label)
        #self.v_layout_esquerda.addWidget(self.formas_edit)

        self.dinheiro_label = QLabel ("Dinheiro")
        self.dinheiro_edit = QLineEdit()
        #self.v_layout_esquerda.addWidget(self.dinheiro_label)
        #self.v_layout_esquerda.addWidget(self.dinheiro_edit)

        #layout vertical da direita
        self.v_layout_direita = QHBoxLayout()

        #labels da direita

        self.restante_label = QLabel ("Restante")
        self.restante_edit = QLineEdit()
        self.v_layout_direita.addWidget(self.restante_label)
        self.v_layout_direita.addWidget(self.restante_edit)


        
        





        #layout horizontal
        #self.v_layout1 = QHBoxLayout()

        #add todos layout da coluna de cima
        #self.label_coluna_cima.setLayout(self.v_layout_cima)
        
        #add todos layout da coluna esquerda
        #self.label_coluna_esquerda.setLayout(self.v_layout_esquerda)

        
        #add todos layout da coluna direita 
        #self.label_coluna_direita.setLayout(self.v_layout_direita)

        #Cria o layout horizontal para as colunas
        

            #add coluna esquerda e direita
        #self.v_layout.addWidget(self.label_coluna_cima)
        self.v_layout.addWidget(self.label_coluna_cima)
        self.v_layout.addWidget(self.label_coluna_embaixo)
        
        
        #add layout a tela
        self.setLayout(self.v_layout)
        
       
                




app = QApplication(sys.argv)
cx = janela()
cx.show()
app.exec_()

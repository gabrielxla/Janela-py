import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QVBoxLayout,QPushButton,QHBoxLayout,QTableView,QBoxLayout,QTableWidget 
from PyQt5.QtGui import QPixmap

class Caixa(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(30,30,1400,800)
        self.setWindowTitle("Caixa da Loja")
        
        #Coluna esquerda
        self.label_coluna_esquerda = QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#bf04b3}")

        #coluna direita
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#bf04b3}")

        #Criar o conteudo da esquerda
        self.v_layout_esquerda = QVBoxLayout ()
        
        #imagem/logo
        self.logo_label = QLabel ()
        self.logo_label.setPixmap(QPixmap("C:/Users/gabriel.landrade2/Documents/JanelaCaixa/.venv/mansao.jpg"))
        #ajustar a imagem
        self.logo_label.setScaledContents(True)
        self.v_layout_esquerda.addWidget(self.logo_label)
        self.logo_label.setFixedHeight(300)
        self.logo_label.setFixedWidth(700)
        

        #label e lines da coluna da esquerda
        self.codigo_produto_label = QLabel("codigo do produto")
        self.codigo_produto_edit = QLineEdit()
        self.codigo_produto_edit.setStyleSheet("QLabel{font-size:20pt;color:#700}")
        self.v_layout_esquerda.addWidget(self.codigo_produto_label)
        self.v_layout_esquerda.addWidget(self.codigo_produto_edit)
        
        self.nome_produto_label = QLabel("nome do produto")
        self.nome_produto_edit = QLineEdit()
        self.nome_produto_edit.setStyleSheet("QLabel{font-size:20pt;color:#700}")
        self.v_layout_esquerda.addWidget(self.nome_produto_label)
        self.v_layout_esquerda.addWidget(self.nome_produto_edit)

        self.descricao_produto_label = QLabel("descrição do produto")
        self.descricao_produto_edit = QLineEdit()
        self.descricao_produto_edit.setStyleSheet("QLabel{font-size:20pt;color:#700}")
        self.v_layout_esquerda.addWidget(self.descricao_produto_label)
        self.v_layout_esquerda.addWidget(self.descricao_produto_edit)

        self.quantidade_produto_label = QLabel("Quantidade do produto")
        self.quantidade_produto_edit = QLineEdit()
        self.quantidade_produto_edit.setStyleSheet("QLabel{font-size:20pt;color:#700}")
        self.v_layout_esquerda.addWidget(self.quantidade_produto_label)
        self.v_layout_esquerda.addWidget(self.quantidade_produto_edit)

        self.preco_produto_label = QLabel("Preço unitario")
        self.preco_produto_edit = QLineEdit()
        self.preco_produto_edit.setStyleSheet("QLabel{font-size:20pt;color:#700}")
        self.v_layout_esquerda.addWidget(self.preco_produto_label)
        self.v_layout_esquerda.addWidget(self.preco_produto_edit)

        self.total_produto_label = QLabel("Total")
        self.total_produto_edit = QLineEdit()
        self.total_produto_edit.setStyleSheet("QLabel{font-size:20pt;color:#700}")
        self.v_layout_esquerda.addWidget(self.total_produto_label)
        self.v_layout_esquerda.addWidget(self.total_produto_edit)

        #------------- controles da coluna da direita ---------------
        self.v_layout_direita = QVBoxLayout()

        #criar tabela
        #colunas
        colunas = ["cod.produto","nome do produto", "Descrição","Quantidade","preço unitario"]
        self.tabela = QTableWidget ()
        self.tabela.setColumnCount(5)
        self.tabela.setHorizontalHeaderLabels(colunas)
        self.tabela.setRowCount(10)
        self.v_layout_direita.addWidget(self.tabela)

        self.total_pagar_label =QLabel("Total a pagar")
        self.total_pagar_edit = QLineEdit()
        self.v_layout_direita.addWidget(self.total_pagar_label)
        self.v_layout_direita.addWidget(self.total_pagar_edit)

        

        self.label_coluna_direita.setLayout(self.v_layout_direita)
        #Cria o layout horizontal para as colunas
        self.h_layout = QHBoxLayout()

        #add coluna esquerda e direita
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)
        
        #add layout a tela
        self.setLayout(self.h_layout)
        
        #add todos layout da coluna esquerda
        self.label_coluna_esquerda.setLayout(self.v_layout_esquerda)

        
        

app = QApplication(sys.argv)
cx = Caixa()
cx.show()
app.exec_()

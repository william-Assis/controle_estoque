from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPalette, QColor, QPixmap, QIcon
import os 
from os.path import join, dirname
from ..utilitarios.estilo_global import (
    aplicar_estilo_global, 
    ESTILO_INPUT, 
    ESTILO_BOTAO,
    obter_fonte_input,
    obter_fonte_botao
)

class TelaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def carregar_imagem(self, caminho, descricao):
        if not os.path.exists(caminho):
            print(f"Erro: Arquivo não encontrado - {caminho}")
            return None
        pixmap = QPixmap(caminho)
        if pixmap.isNull():
            print(f"Erro: Falha ao carregar imagem - {descricao}")
            return None
        return pixmap

    def carregar_icone(self, caminho, descricao):
        if not os.path.exists(caminho):
            print(f"Erro: Arquivo não encontrado - {caminho}")
            return QIcon()
        icone = QIcon(caminho)
        if icone.isNull():
            print(f"Erro: Falha ao carregar ícone - {descricao}")
            return QIcon()
        return icone
        
    def initUI(self):
        # Configurando o tamanho da janela
        self.setFixedSize(600, 700)
        
        # Configurando a cor de fundo (#129ACF)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('#129ACF'))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        
        # Configurando o título da janela
        self.setWindowTitle('Login - Controle de Estoque')
        
        # Centralizando a janela na tela
        self.center()
        
        # Adicionando a logo com validação
        logo_path = join(dirname(dirname(dirname(__file__))), 'recursos', 'imagens', 'logos', 'logo_tela_login.png')
        logo_pixmap = self.carregar_imagem(logo_path, "Logo do login")
        if logo_pixmap:
            logo_label = QLabel(self)
            logo_label.setPixmap(logo_pixmap)
            logo_label.setGeometry(86, 30, logo_pixmap.width(), logo_pixmap.height())
        else:
            # Criar um label com texto alternativo caso a imagem falhe
            logo_label = QLabel("Sistema de Controle de Estoque", self)
            logo_label.setGeometry(86, 30, 400, 100)
            logo_label.setStyleSheet("color: white; font-size: 24px;")
            
        # Criando o campo de entrada de usuário
        input_usuario = QLineEdit(self)
        posicao_y = logo_label.y() + logo_label.height() + 50
        input_usuario.setGeometry(50, posicao_y, 500, 80)
        input_usuario.setPlaceholderText("USUÁRIO")
        
        # Configurando o estilo do input_usuario
        input_usuario.setFont(obter_fonte_input())
        input_usuario.setTextMargins(30, 0, 0, 0)
        input_usuario.setStyleSheet(ESTILO_INPUT)
            
        # Criando o campo de entrada de senha
        input_senha = QLineEdit(self)
        input_senha.setGeometry(50, posicao_y + 80 + 45, 500, 80)  # 45px abaixo do input de usuário
        input_senha.setPlaceholderText("SENHA")
        input_senha.setEchoMode(QLineEdit.Password)  # Para ocultar a senha
        
        # Configurando o estilo do input_senha
        input_senha.setFont(obter_fonte_input())
        input_senha.setTextMargins(30, 0, 0, 0)
        input_senha.setStyleSheet(ESTILO_INPUT)
        
        # Criando o botão ENTRAR
        self.botao_entrar = QPushButton('ENTRAR', self)
        self.botao_entrar.setGeometry(100, input_senha.y() + 80 + 45, 400, 80)
        # Configurando o estilo do botão
        self.botao_entrar.setFont(obter_fonte_botao())
        self.botao_entrar.setStyleSheet(ESTILO_BOTAO)
        
        # Carregando o ícone com validação
        icone_path = join(dirname(dirname(dirname(__file__))), 'recursos', 'imagens', 'icones', 'icone_button_login.png')
        self.icone = self.carregar_icone(icone_path, "Ícone do botão de login")
        
        # Configurando o botão com ícone inicial (invisível)
        self.botao_entrar.setIcon(self.icone)
        self.botao_entrar.setIconSize(QSize(24, 0))
        
        # Conectando o evento de hover
        self.botao_entrar.enterEvent = self.botao_hover_enter
        self.botao_entrar.leaveEvent = self.botao_hover_leave

    def botao_hover_enter(self, event):
        self.botao_entrar.setIconSize(QSize(24, 24))  # Torna o ícone visível

    def botao_hover_leave(self, event):
        self.botao_entrar.setIconSize(QSize(24, 0))  # Torna o ícone invisível
        self.botao_entrar.setStyleSheet(ESTILO_BOTAO)

    def center(self):
        # Método para centralizar a janela na tela
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    aplicar_estilo_global()  # Aplicando o estilo global
    login = TelaLogin()
    login.show()
    sys.exit(app.exec_())
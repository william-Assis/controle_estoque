from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont

# Constantes de Estilo
ESTILO_INPUT = """
    QLineEdit { 
        border-radius: 15px; 
        border: none;
    }
    QLineEdit:focus {
        border: 2px solid black;
    }
"""

ESTILO_BOTAO = """
    QPushButton {
        background-color: #3F3B3B;
        color: #FFFFFF;
        border-radius: 15px;
        border: none;
        text-align: center;
        padding: 0px;
    }
    QPushButton:pressed {
        background-color: #4F4B4B;
    }
"""

# Constantes de Fonte
TAMANHO_FONTE_PADRAO = 16
TAMANHO_FONTE_INPUT = 20
TAMANHO_FONTE_BOTAO = 20

def aplicar_estilo_global():
    # Configuração da fonte global
    fonte_global = QFont()
    fonte_global.setFamily("Segoe UI Variable, Segoe UI, Roboto")
    fonte_global.setPointSize(TAMANHO_FONTE_PADRAO)
    QApplication.setFont(fonte_global)

def obter_fonte_input():
    fonte = QFont()
    fonte.setPointSize(TAMANHO_FONTE_INPUT)
    fonte.setBold(True)
    return fonte

def obter_fonte_botao():
    fonte = QFont()
    fonte.setPointSize(TAMANHO_FONTE_BOTAO)
    fonte.setBold(True)
    return fonte

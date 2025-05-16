from src.interface.tela_login import TelaLogin
from PyQt5.QtWidgets import QApplication
from src.utilitarios.estilo_global import aplicar_estilo_global
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    aplicar_estilo_global()
    login = TelaLogin()
    login.show()
    sys.exit(app.exec_())
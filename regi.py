"""
Il file Python che fa funzionare l'intero programma. Per ora è completamente vuoto: sono stati inseriti solo i comandi necessari all'inizializzazione.
"""
import sys
from PyQt5 import QtWidgets
from regi0 import Ui_MainWindow   # questa riga importa la struttura dell'UI in formato .py!!!

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\regi_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from peewee import *
import esp_db
import esp_infissi

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1300, 860))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pag_0 = QtWidgets.QWidget()
        self.pag_0.setObjectName("pag_0")
        self.pushButton_2 = QtWidgets.QPushButton(self.pag_0)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 250, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.pag_0)
        self.pushButton.setGeometry(QtCore.QRect(60, 210, 150, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(self.pag_0)
        self.listView.setGeometry(QtCore.QRect(330, 210, 250, 200))
        self.listView.setObjectName("listView")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.pag_0)
        self.commandLinkButton.setGeometry(QtCore.QRect(340, 220, 172, 41))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.pag_0)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 370, 191, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.pag_0)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 310, 191, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.pag_0)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.pag_0)
        self.label_4.setGeometry(QtCore.QRect(330, 150, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.pag_0)
        self.pag_1 = QtWidgets.QWidget()
        self.pag_1.setObjectName("pag_1")
        self.tab_clienti = QtWidgets.QTableWidget(self.pag_1)
        self.tab_clienti.setGeometry(QtCore.QRect(20, 80, 1250, 451))
        self.tab_clienti.setObjectName("tab_clienti")
        self.tab_clienti.setColumnCount(8)
        self.tab_clienti.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_clienti.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_clienti.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_clienti.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_clienti.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_clienti.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_clienti.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_clienti.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_clienti.setHorizontalHeaderItem(7, item)
        self.btn_agg_cliente = QtWidgets.QPushButton(self.pag_1)
        self.btn_agg_cliente.setGeometry(QtCore.QRect(90, 560, 150, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_agg_cliente.setFont(font)
        self.btn_agg_cliente.setObjectName("btn_agg_cliente")
        self.label = QtWidgets.QLabel(self.pag_1)
        self.label.setGeometry(QtCore.QRect(29, 570, 51, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.pag_1)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.pag_1)
        self.pag_2 = QtWidgets.QWidget()
        self.pag_2.setObjectName("pag_2")
        self.stackedWidget.addWidget(self.pag_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 20))
        self.menubar.setObjectName("menubar")
        self.menuNuovo = QtWidgets.QMenu(self.menubar)
        self.menuNuovo.setObjectName("menuNuovo")
        self.menuRecenti = QtWidgets.QMenu(self.menuNuovo)
        self.menuRecenti.setObjectName("menuRecenti")
        self.menuNuovo_2 = QtWidgets.QMenu(self.menuNuovo)
        self.menuNuovo_2.setObjectName("menuNuovo_2")
        self.menuInserisci = QtWidgets.QMenu(self.menubar)
        self.menuInserisci.setObjectName("menuInserisci")
        self.menuVista = QtWidgets.QMenu(self.menubar)
        self.menuVista.setObjectName("menuVista")
        self.menuAnteprima = QtWidgets.QMenu(self.menubar)
        self.menuAnteprima.setObjectName("menuAnteprima")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVersione = QtWidgets.QAction(MainWindow)
        self.actionVersione.setObjectName("actionVersione")
        self.actionVerifica_aggiornamenti = QtWidgets.QAction(MainWindow)
        self.actionVerifica_aggiornamenti.setObjectName("actionVerifica_aggiornamenti")
        self.actionApri = QtWidgets.QAction(MainWindow)
        self.actionApri.setObjectName("actionApri")
        self.actionRecente_1 = QtWidgets.QAction(MainWindow)
        self.actionRecente_1.setObjectName("actionRecente_1")
        self.actionRecente_2 = QtWidgets.QAction(MainWindow)
        self.actionRecente_2.setObjectName("actionRecente_2")
        self.actionDa_zero = QtWidgets.QAction(MainWindow)
        self.actionDa_zero.setObjectName("actionDa_zero")
        self.actionDa_precompilato = QtWidgets.QAction(MainWindow)
        self.actionDa_precompilato.setObjectName("actionDa_precompilato")
        self.actionInfisso = QtWidgets.QAction(MainWindow)
        self.actionInfisso.setObjectName("actionInfisso")
        self.actionDark_Mode = QtWidgets.QAction(MainWindow)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.actionVisualizza_anteprima_di_stampa = QtWidgets.QAction(MainWindow)
        self.actionVisualizza_anteprima_di_stampa.setObjectName("actionVisualizza_anteprima_di_stampa")
        self.menuRecenti.addAction(self.actionRecente_1)
        self.menuRecenti.addAction(self.actionRecente_2)
        self.menuNuovo_2.addAction(self.actionDa_zero)
        self.menuNuovo_2.addAction(self.actionDa_precompilato)
        self.menuNuovo.addAction(self.menuNuovo_2.menuAction())
        self.menuNuovo.addAction(self.actionApri)
        self.menuNuovo.addAction(self.menuRecenti.menuAction())
        self.menuInserisci.addAction(self.actionInfisso)
        self.menuVista.addAction(self.actionDark_Mode)
        self.menuAnteprima.addAction(self.actionVisualizza_anteprima_di_stampa)
        self.menuInfo.addAction(self.actionVersione)
        self.menuInfo.addAction(self.actionVerifica_aggiornamenti)
        self.menubar.addAction(self.menuNuovo.menuAction())
        self.menubar.addAction(self.menuInserisci.menuAction())
        self.menubar.addAction(self.menuVista.menuAction())
        self.menubar.addAction(self.menuAnteprima.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1)) # funziona!
        self.pushButton.clicked.connect(self.loadDB)

    def loadDB(self):
        esp_db.db.connect()
        query = esp_db.Cliente.select().dicts() # risultato:
        # ({'id': 1, 'cognome': 'Dimaglie', "nome":"Gregorio" ecc.}, ecc.)
        for num_riga, cliente in enumerate(query):
            self.tab_clienti.insertRow(num_riga)
            for i in range(len(query)):
                pass
        # for num_riga, cliente in enumerate(query):
        #     self.tab_clienti.insertRow(num_riga)
        #     for num_colonna, dato in enumerate(cliente.values):
        #         self.tab_clienti.setItem(num_riga, num_colonna, QtWidgets.QTableWidgetItem(str(cliente.dato)))
        esp_db.db.close()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Apri preventivo..."))
        self.pushButton.setText(_translate("MainWindow", "Nuovo preventivo..."))
        self.commandLinkButton.setText(_translate("MainWindow", "CommandLinkButton 1"))
        self.pushButton_4.setText(_translate("MainWindow", "Informazioni sul prodotto"))
        self.pushButton_3.setText(_translate("MainWindow", "Visualizza anagrafica clienti"))
        self.label_3.setText(_translate("MainWindow", "Inizia"))
        self.label_4.setText(_translate("MainWindow", "Aperti di recente"))
        item = self.tab_clienti.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cognome"))
        item = self.tab_clienti.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tab_clienti.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Via"))
        item = self.tab_clienti.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Comune"))
        item = self.tab_clienti.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tel. 1"))
        item = self.tab_clienti.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Tel. 2"))
        item = self.tab_clienti.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tab_clienti.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Cantiere"))
        self.btn_agg_cliente.setText(_translate("MainWindow", "Aggiungi cliente..."))
        self.label.setText(_translate("MainWindow", "Oppure"))
        self.label_2.setText(_translate("MainWindow", "Seleziona un cliente"))
        self.menuNuovo.setTitle(_translate("MainWindow", "File"))
        self.menuRecenti.setTitle(_translate("MainWindow", "Recenti"))
        self.menuNuovo_2.setTitle(_translate("MainWindow", "Nuovo..."))
        self.menuInserisci.setTitle(_translate("MainWindow", "Inserisci"))
        self.menuVista.setTitle(_translate("MainWindow", "Vista"))
        self.menuAnteprima.setTitle(_translate("MainWindow", "Anteprima"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.actionVersione.setText(_translate("MainWindow", "Versione..."))
        self.actionVerifica_aggiornamenti.setText(_translate("MainWindow", "Verifica aggiornamenti..."))
        self.actionApri.setText(_translate("MainWindow", "Apri..."))
        self.actionRecente_1.setText(_translate("MainWindow", "Recente 1"))
        self.actionRecente_2.setText(_translate("MainWindow", "Recente 2"))
        self.actionDa_zero.setText(_translate("MainWindow", "Da zero"))
        self.actionDa_precompilato.setText(_translate("MainWindow", "Da precompilato"))
        self.actionInfisso.setText(_translate("MainWindow", "Infisso..."))
        self.actionDark_Mode.setText(_translate("MainWindow", "Dark Mode"))
        self.actionVisualizza_anteprima_di_stampa.setText(_translate("MainWindow", "Visualizza anteprima di stampa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

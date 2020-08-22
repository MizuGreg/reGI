# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_scegli_testo.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 681, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_testi = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tab_testi.setMinimumSize(QtCore.QSize(0, 250))
        self.tab_testi.setObjectName("tab_testi")
        self.tab_testi.setColumnCount(2)
        self.tab_testi.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_testi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_testi.setHorizontalHeaderItem(1, item)
        self.tab_testi.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tab_testi)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.edit_testo_selez = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.edit_testo_selez.setEnabled(True)
        self.edit_testo_selez.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.edit_testo_selez.setReadOnly(True)
        self.edit_testo_selez.setObjectName("edit_testo_selez")
        self.horizontalLayout_2.addWidget(self.edit_testo_selez)
        self.btn_fatto = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fatto.sizePolicy().hasHeightForWidth())
        self.btn_fatto.setSizePolicy(sizePolicy)
        self.btn_fatto.setMinimumSize(QtCore.QSize(80, 40))
        self.btn_fatto.setObjectName("btn_fatto")
        self.horizontalLayout_2.addWidget(self.btn_fatto)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_aggiungi = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_aggiungi.sizePolicy().hasHeightForWidth())
        self.btn_aggiungi.setSizePolicy(sizePolicy)
        self.btn_aggiungi.setMinimumSize(QtCore.QSize(80, 40))
        self.btn_aggiungi.setFlat(False)
        self.btn_aggiungi.setObjectName("btn_aggiungi")
        self.horizontalLayout.addWidget(self.btn_aggiungi)
        self.btn_modifica = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_modifica.sizePolicy().hasHeightForWidth())
        self.btn_modifica.setSizePolicy(sizePolicy)
        self.btn_modifica.setMinimumSize(QtCore.QSize(80, 40))
        self.btn_modifica.setObjectName("btn_modifica")
        self.horizontalLayout.addWidget(self.btn_modifica)
        self.btn_elimina = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_elimina.sizePolicy().hasHeightForWidth())
        self.btn_elimina.setSizePolicy(sizePolicy)
        self.btn_elimina.setMinimumSize(QtCore.QSize(80, 40))
        self.btn_elimina.setObjectName("btn_elimina")
        self.horizontalLayout.addWidget(self.btn_elimina)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_scegli = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_scegli.sizePolicy().hasHeightForWidth())
        self.btn_scegli.setSizePolicy(sizePolicy)
        self.btn_scegli.setMinimumSize(QtCore.QSize(80, 40))
        self.btn_scegli.setObjectName("btn_scegli")
        self.horizontalLayout.addWidget(self.btn_scegli)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Scegli il testo iniziale/finale del preventivo"))
        self.tab_testi.setWhatsThis(_translate("Dialog", "Tabella che custodisce i testi iniziali/finali da inserire all\'inizio e alla fine di ogni preventivo."))
        item = self.tab_testi.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tab_testi.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Testo"))
        self.edit_testo_selez.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Thfeaounfaenfoeanfoaenfoaen oae ea.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">faoehnfjeafoaehno uahjfuoeahouifhe ouaehjfuoeahjof aehfoupejfouaehj oao.</span></p></body></html>"))
        self.btn_fatto.setText(_translate("Dialog", "Fatto"))
        self.btn_aggiungi.setText(_translate("Dialog", "Aggiungi"))
        self.btn_modifica.setText(_translate("Dialog", "Modifica"))
        self.btn_elimina.setText(_translate("Dialog", "Elimina"))
        self.btn_scegli.setText(_translate("Dialog", "Scegli"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

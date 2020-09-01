### ALL'INIZIO

from PyQt5 import QtCore, QtGui, QtWidgets

import sentry_sdk
sentry_sdk.init("https://d770165f943e497484a6fa95ebcef724@o429982.ingest.sentry.io/5377715")
from regi_db import db, Value, Cliente, Preventivo, TestoIn, TestoFin, Progetto, Infisso
from regi_db import model_to_dict
from datetime import date

class TreeItem(QtGui.QStandardItem):
    def __init__(self, txt = "", font_size = 12, set_bold = False, color = QtGui.QColor(0, 0, 0)):
        super().__init__()
        self.setEditable(False)
        fnt = QtGui.QFont("Open Sans", font_size)
        fnt.setBold(set_bold)
        self.setFont(fnt)
        self.setText(txt)
        self.setForeground(color)

class DialogAggCliente(QtWidgets.QDialog): 
    def __init__(self, parent=None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.resize(600, 200)
        self.edit_cognome = QtWidgets.QLineEdit()
        self.edit_nome = QtWidgets.QLineEdit()
        self.edit_via = QtWidgets.QLineEdit()
        self.edit_comune = QtWidgets.QLineEdit()
        self.edit_tel1 = QtWidgets.QLineEdit()
        self.edit_tel2 = QtWidgets.QLineEdit()
        self.edit_email = QtWidgets.QLineEdit()
        self.edit_cantiere = QtWidgets.QLineEdit()
        layout_agg_cliente = QtWidgets.QFormLayout()
        layout_agg_cliente.addRow("Cognome", self.edit_cognome)
        layout_agg_cliente.addRow("Nome", self.edit_nome)
        layout_agg_cliente.addRow("Via", self.edit_via)
        layout_agg_cliente.addRow("Comune", self.edit_comune)
        layout_agg_cliente.addRow("Telefono 1", self.edit_tel1)
        layout_agg_cliente.addRow("Telefono 2", self.edit_tel2)
        layout_agg_cliente.addRow("Email", self.edit_email)
        layout_agg_cliente.addRow("Cantiere", self.edit_cantiere)
        self.bottoni = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.bottoni.accepted.connect(self.controlla)
        self.bottoni.rejected.connect(self.reject)
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(layout_agg_cliente)
        layout.addWidget(self.bottoni)
        self.setLayout(layout)
    def popup_nome_mancante(self):
        popup = QtWidgets.QMessageBox()
        popup.resize(600, 300)
        popup.setWindowTitle("Parametri non corretti")
        popup.setText("Per caricare i dati nell'archivio sono necessari almeno i seguenti dati: Cognome, Nome. Si prega di riempire questi campi.")
        popup.setIcon(QtWidgets.QMessageBox.Information)
        x = popup.exec_()
    def controlla(self):
        if self.edit_cognome.text() == "" or self.edit_nome.text() == "":
            self.popup_nome_mancante()
        else:
            self.cliente_nuovo = {"cognome": self.edit_cognome.text(),
                            "nome": self.edit_nome.text(),
                            "via": self.edit_via.text(),
                            "comune": self.edit_comune.text(),
                            "tel1": self.edit_tel1.text(),
                            "tel2": self.edit_tel2.text(),
                            "email": self.edit_email.text(),
                            "cantiere": self.edit_cantiere.text()}
            self.accept()

class DialogEditCliente(QtWidgets.QDialog): 
    def __init__(self, parent=None):
        super(QtWidgets.QDialog, self).__init__(parent)
        self.resize(600, 200)
        self.edit_cognome = QtWidgets.QLineEdit()
        self.edit_nome = QtWidgets.QLineEdit()
        self.edit_via = QtWidgets.QLineEdit()
        self.edit_comune = QtWidgets.QLineEdit()
        self.edit_tel1 = QtWidgets.QLineEdit()
        self.edit_tel2 = QtWidgets.QLineEdit()
        self.edit_email = QtWidgets.QLineEdit()
        self.edit_cantiere = QtWidgets.QLineEdit()
        self.edit_cognome.setText(ui.current_cliente["cognome"])
        self.edit_nome.setText(ui.current_cliente["nome"])
        self.edit_via.setText(ui.current_cliente["via"])
        self.edit_comune.setText(ui.current_cliente["comune"])
        self.edit_tel1.setText(ui.current_cliente["tel1"])
        self.edit_tel2.setText(ui.current_cliente["tel2"])
        self.edit_email.setText(ui.current_cliente["email"])
        self.edit_cantiere.setText(ui.current_cliente["cantiere"])
        layout_edit_cliente = QtWidgets.QFormLayout()
        layout_edit_cliente.addRow("Cognome", self.edit_cognome)
        layout_edit_cliente.addRow("Nome", self.edit_nome)
        layout_edit_cliente.addRow("Via", self.edit_via)
        layout_edit_cliente.addRow("Comune", self.edit_comune)
        layout_edit_cliente.addRow("Telefono 1", self.edit_tel1)
        layout_edit_cliente.addRow("Telefono 2", self.edit_tel2)
        layout_edit_cliente.addRow("Email", self.edit_email)
        layout_edit_cliente.addRow("Cantiere", self.edit_cantiere)
        self.bottoni = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.bottoni.accepted.connect(self.controlla)
        self.bottoni.rejected.connect(self.reject)
        layout = QtWidgets.QVBoxLayout()
        layout.addLayout(layout_edit_cliente)
        layout.addWidget(self.bottoni)
        self.setLayout(layout)
    def popup_nome_mancante(self):
        popup = QtWidgets.QMessageBox()
        popup.resize(600, 300)
        popup.setWindowTitle("Parametri non corretti")
        popup.setText("Per caricare i dati nell'archivio sono necessari almeno i seguenti dati: Cognome, Nome. Si prega di riempire questi campi.")
        popup.setIcon(QtWidgets.QMessageBox.Information)
        x = popup.exec_()
    def controlla(self):
        if self.edit_cognome.text() == "" or self.edit_nome.text() == "":
            self.popup_nome_mancante()
        else:
            self.cliente_modificato = {"cognome": self.edit_cognome.text(),
                            "nome": self.edit_nome.text(),
                            "via": self.edit_via.text(),
                            "comune": self.edit_comune.text(),
                            "tel1": self.edit_tel1.text(),
                            "tel2": self.edit_tel2.text(),
                            "email": self.edit_email.text(),
                            "cantiere": self.edit_cantiere.text()}
            self.accept()

class DialogScegliTesto(QtWidgets.QDialog): 
    def __init__(self, parent = None):
        super(QtWidgets.QDialog, self).__init__(parent)

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 681, 481))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.tab_testi = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tab_testi.setMinimumSize(QtCore.QSize(0, 250))
        self.tab_testi.setColumnCount(2)
        self.tab_testi.setRowCount(0)
        self.tab_testi.setHorizontalHeaderLabels(["ID", "Testo"])
        self.tab_testi.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tab_testi)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.edit_testo_selez = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.edit_testo_selez.setEnabled(True)
        self.edit_testo_selez.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.edit_testo_selez.setReadOnly(True)
        self.horizontalLayout_2.addWidget(self.edit_testo_selez)
        self.btn_fatto = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_fatto.setText("Fatto")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fatto.sizePolicy().hasHeightForWidth())
        self.btn_fatto.setSizePolicy(sizePolicy)
        self.btn_fatto.setMinimumSize(QtCore.QSize(80, 40))
        self.horizontalLayout_2.addWidget(self.btn_fatto)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.btn_aggiungi = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_aggiungi.setText("Aggiungi")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_aggiungi.sizePolicy().hasHeightForWidth())
        self.btn_aggiungi.setSizePolicy(sizePolicy)
        self.btn_aggiungi.setMinimumSize(QtCore.QSize(80, 40))
        self.horizontalLayout.addWidget(self.btn_aggiungi)
        self.btn_modifica = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_modifica.setText("Modifica")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_modifica.sizePolicy().hasHeightForWidth())
        self.btn_modifica.setSizePolicy(sizePolicy)
        self.btn_modifica.setMinimumSize(QtCore.QSize(80, 40))
        self.horizontalLayout.addWidget(self.btn_modifica)
        self.btn_elimina = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_elimina.setText("Elimina")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_elimina.sizePolicy().hasHeightForWidth())
        self.btn_elimina.setSizePolicy(sizePolicy)
        self.btn_elimina.setMinimumSize(QtCore.QSize(80, 40))
        self.horizontalLayout.addWidget(self.btn_elimina)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_scegli = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_scegli.setText("Scegli")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_scegli.sizePolicy().hasHeightForWidth())
        self.btn_scegli.setSizePolicy(sizePolicy)
        self.btn_scegli.setMinimumSize(QtCore.QSize(80, 40))
        self.horizontalLayout.addWidget(self.btn_scegli)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.operazione = ""
        self.popola_tabella()
        self.tab_testi.cellClicked.connect(self.popola_edit)
        self.btn_aggiungi.clicked.connect(self.aggiungi)
        self.btn_modifica.clicked.connect(self.modifica)
        self.btn_elimina.clicked.connect(self.elimina)
        self.btn_fatto.clicked.connect(self.fatto)
        self.btn_scegli.clicked.connect(self.scegli)
    
    def popola_tabella(self):
        if ui.quale_testo == "in":
            lista_testi = TestoIn.select().dicts()
        else:
            lista_testi = TestoFin.select().dicts()
        for num_riga, voce in enumerate(lista_testi):
            self.tab_testi.insertRow(num_riga)
            self.tab_testi.setItem(num_riga, 0, QtWidgets.QTableWidgetItem(str(voce["id"]).zfill(4)))
            self.tab_testi.setItem(num_riga, 1, QtWidgets.QTableWidgetItem(voce["testo"][:100]))

    def popola_edit(self):
        if self.tab_testi.currentRow() == -1:
            self.popup_testo("Nessun testo selezionato")
        elif self.operazione == "":
            id_testo_selez = self.tab_testi.item(self.tab_testi.currentRow(), 0).text()
            if ui.quale_testo == "in":
                voce_selez = TestoIn.get(TestoIn.id == id_testo_selez)
            else:
                voce_selez = TestoFin.get(TestoFin.id == id_testo_selez)
            self.edit_testo_selez.setPlainText(voce_selez.testo)

    def popup_testo(self, titolo):
        popup = QtWidgets.QMessageBox()
        popup.resize(600, 300)
        popup.setWindowTitle(titolo)
        if titolo == "Nessun testo selezionato":
            popup.setText("Selezionare un testo per modificarlo o eliminarlo.")
        elif titolo == "Testo vuoto":
            popup.setText("Il contenuto del testo non può essere vuoto.")
        popup.setIcon(QtWidgets.QMessageBox.Information)
        x = popup.exec_()

    def aggiungi(self):
        self.operazione = "aggiungi"
        self.btn_modifica.setEnabled(False)
        self.btn_elimina.setEnabled(False)
        self.btn_scegli.setEnabled(False)
        self.edit_testo_selez.setPlainText("")
        self.edit_testo_selez.setReadOnly(False)
        self.edit_testo_selez.setFrameShape(QtWidgets.QFrame.StyledPanel)


    def modifica(self):
        self.operazione = "modifica"
        self.btn_aggiungi.setEnabled(False)
        self.btn_elimina.setEnabled(False)
        self.btn_scegli.setEnabled(False)
        self.edit_testo_selez.setFrameShape(QtWidgets.QFrame.StyledPanel)

    def elimina(self):
        if self.tab_testi.currentRow() == -1:
            self.popup_testo("Nessun testo selezionato")
        else:
            id_testo_canc = self.tab_testi.item(self.tab_testi.currentRow(), 0).text()
            if ui.quale_testo == "in":
                TestoIn.get(TestoIn.id == id_testo_canc).delete_instance()
            else:
                TestoFin.get(TestoFin.id == id_testo_canc).delete_instance()
            self.tab_testi.removeRow(self.tab_testi.currentRow())

    def fatto(self):
        if self.edit_testo_selez.toPlainText() == "":
            self.popup_testo("Testo vuoto")
        
        elif self.operazione == "aggiungi":
            if ui.quale_testo == "in":
                t = model_to_dict(TestoIn.create(testo = self.edit_testo_selez.toPlainText()))
            else:
                t = model_to_dict(TestoFin.create(testo = self.edit_testo_selez.toPlainText()))
            num_riga = self.tab_testi.rowCount()
            self.tab_testi.insertRow(num_riga)
            self.tab_testi.setItem(num_riga, 0, QtWidgets.QTableWidgetItem(str(t["id"]).zfill(4)))
            self.tab_testi.setItem(num_riga, 1, QtWidgets.QTableWidgetItem(t["testo"]))
            self.btn_modifica.setEnabled(True)
            self.btn_elimina.setEnabled(True)
            self.btn_scegli.setEnabled(True)

        elif self.operazione == "modifica":
            num_riga = self.tab_testi.currentRow()
            id_testo_modificato = self.tab_testi.item(num_riga, 0).text()
            testo_modificato = self.edit_testo_selez.toPlainText()
            if ui.quale_testo == "in":
                query = TestoIn.update(testo_modificato).where(TestoIn.id == id_testo_modificato)
            else:
                query = TestoFin.update(testo_modificato).where(TestoFin.id == id_testo_modificato)
            query.execute()
            self.tab_testi.setItem(num_riga, 1, QtWidgets.QTableWidgetItem(testo_modificato[:100]))
            self.btn_aggiungi.setEnabled(True)
            self.btn_elimina.setEnabled(True)
            self.btn_scegli.setEnabled(True)

        self.operazione = ""
        self.edit_testo_selez.setReadOnly(True)
        self.edit_testo_selez.setFrameShape(QtWidgets.QFrame.NoFrame)

    def scegli(self):
        self.testo_da_passare = self.edit_testo_selez.toPlainText()
        self.accept()

### IN QUESTO ORDINE

    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> #

        self.stackedWidget.setCurrentIndex(0)
        self.current_cliente = {"id": 0, "cognome": "", "nome": "", "via": "", "comune": "", "tel1": "", "tel2": "", "email": "", "cantiere": ""}
        self.current_prev = {"id": 0, "cliente": 0, "nick_cliente": "", "anno": 0, "so": 0, "po": 0, "data": "", "testo_in": "", "testo_out": "",
                                "iva": 0.0}
        self.lista_infissi = []
        self.current_index = -1
        self.safe_exit = False

        self.btn_nuovo_prev.clicked.connect(self.view_db_clienti)
        self.btn_view_anagrafica.clicked.connect(self.view_anagrafica)
        self.btn_sc_agg_cliente.clicked.connect(self.sc_agg_cliente)
        self.btn_sc_edit_cliente.clicked.connect(self.sc_edit_cliente)

        self.btn_scegli_cliente.clicked.connect(self.crea_prev)
        self.btn_agg_cliente.clicked.connect(self.agg_cliente)
        self.btn_edit_cliente.clicked.connect(self.edit_cliente)
        self.btn_canc_cliente.clicked.connect(self.canc_cliente)

        self.btn_deduci_so.clicked.connect(self.deduci_SO)
        self.btn_deduci_po.clicked.connect(self.deduci_PO)
        self.btn_deduci_data.clicked.connect(self.deduci_data)
        self.btn_deduci_nick_cliente.clicked.connect(self.deduci_nick_cliente)
        self.btn_deduci_testo_in.clicked.connect(self.deduci_testo_in)
        self.btn_scegli_testo_in.clicked.connect(self.scegli_testo_in)
        self.btn_deduci_testo_fin.clicked.connect(self.deduci_testo_fin)
        self.btn_scegli_testo_fin.clicked.connect(self.scegli_testo_fin)

        self.btn_scegli_progetto.clicked.connect(self.scegli_progetto)
        self.btn_deduci_descr.clicked.connect(self.deduci_descr)
        self.listwidget_infissi.itemClicked.connect(self.load_infisso)
        self.radio_prezzo_listino.toggled.connect(self.tgl_prezzo_listino)
        self.radio_prezzo_custom.toggled.connect(self.tgl_prezzo_custom)
        self.radio_sconto.toggled.connect(self.tgl_sconto)
        self.radio_sconto_percent.toggled.connect(self.tgl_sconto_percent)
        self.btn_salva_prev.clicked.connect(self.salva_prev) # provare senza x


        self.modello_tree_progetti = QtGui.QStandardItemModel()
        self.tree_progetti.setModel(self.modello_tree_progetti)
        self.root_node = self.modello_tree_progetti.invisibleRootItem()

    def view_db_clienti(self):
        self.stackedWidget.setCurrentIndex(1)
        lista_clienti = Cliente.select().dicts()
        for num_riga, cliente in enumerate(lista_clienti):
            self.tab_clienti.insertRow(num_riga)
            for num_colonna, dato in enumerate(cliente.values()):
                if type(dato) is int:
                    dato = str(dato)
                    dato = dato.zfill(4)
                if dato == None or dato == "":
                    dato = "N/A"
                self.tab_clienti.setItem(num_riga, num_colonna, QtWidgets.QTableWidgetItem(dato))
    
    def view_anagrafica(self):
        self.view_db_clienti()
        self.label_2.enabled = False
        self.btn_scegli_cliente.enabled = False
    
    def sc_agg_cliente(self):
        self.view_db_clienti()
        self.label_2.enabled = False
        self.btn_scegli_cliente.enabled = False
        self.btn_edit_cliente.enabled = False
        self.btn_canc_cliente.enabled = False
    
    def sc_edit_cliente(self):
        self.view_db_clienti()
        self.label_2.enabled = False
        self.btn_scegli_cliente.enabled = False
        self.btn_agg_cliente.enabled = False
        self.btn_canc_cliente.enabled = False
    
    def agg_cliente(self):
        dialog = DialogAggCliente()
        if dialog.exec_() != 0:
            cliente_nuovo = dialog.cliente_nuovo
            c = model_to_dict(Cliente.create(**cliente_nuovo))
            num_riga = self.tab_clienti.rowCount()
            self.tab_clienti.insertRow(num_riga) 
            for num_colonna, dato in enumerate(c.values()):
                    if type(dato) is int:
                        dato = str(dato)
                        dato = dato.zfill(4)
                    if dato == None or dato == "":
                        dato = "N/A"
                    self.tab_clienti.setItem(num_riga, num_colonna, QtWidgets.QTableWidgetItem(dato))
    
    def popup_nessun_cliente(self):
        popup = QtWidgets.QMessageBox()
        popup.resize(600, 300)
        popup.setWindowTitle("Nessun cliente selezionato")
        popup.setText("Selezionare un cliente dalla tabella per modificare i dati o eliminare la voce.")
        popup.setIcon(QtWidgets.QMessageBox.Information)
        x = popup.exec_()
    
    def popup_conferma(self):
        popup = QtWidgets.QMessageBox()
        popup.resize(600, 300)
        popup.setWindowTitle("Azione irreversibile")
        popup.setText("Attenzione, la cancellazione di un cliente non è reversibile. Procedere?")
        popup.setIcon(QtWidgets.QMessageBox.Warning)
        popup.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        popup.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        popup.buttonClicked.connect(self.show_popup_btn)
        x = popup.exec_()
    
    def popup_salva_prev(self):
        popup = QtWidgets.QMessageBox()
        popup.resize(600, 300)
        popup.setWindowTitle("Azione irreversibile")
        popup.setText("Attenzione, quest'azione sovrascriverà i dati precedenti. Procedere?")
        popup.setIcon(QtWidgets.QMessageBox.Warning)
        popup.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        popup.setDefaultButton(QtWidgets.QMessageBox.Cancel)
        popup.buttonClicked.connect(self.show_popup_btn)
        x = popup.exec_()
    
    def show_popup_btn(self, item):
        self.bool_conferma = item.text() == "OK"
    
    def edit_cliente(self):
        if self.tab_clienti.currentRow() == -1:
            self.popup_nessun_cliente()
        else:
            num_riga = self.tab_clienti.currentRow()
            id_cliente_edit = self.tab_clienti.item(self.tab_clienti.currentRow(), 0).text()
            self.current_cliente = model_to_dict(Cliente.get(Cliente.id == id_cliente_edit))
            dialog = DialogEditCliente()
            if dialog.exec_() != 0:
                cliente_modificato = dialog.cliente_modificato
                query = Cliente.update(cliente_modificato).where(Cliente.id == id_cliente_edit)
                query.execute()
                c = model_to_dict(Cliente.get(Cliente.id == id_cliente_edit))
                for num_colonna, dato in enumerate(c.values()):
                    if type(dato) is int:
                        dato = str(dato)
                        dato = dato.zfill(4)
                    if dato == None or dato == "":
                        dato = "N/A"
                    self.tab_clienti.setItem(num_riga, num_colonna, QtWidgets.QTableWidgetItem(dato))
    
    def canc_cliente(self):
        if self.tab_clienti.currentRow() == -1:
            self.popup_nessun_cliente()
        else:
            self.bool_conferma = 0
            self.popup_conferma()
            if self.bool_conferma:
                id_cliente_canc = self.tab_clienti.item(self.tab_clienti.currentRow(), 0).text()
                Cliente.get(Cliente.id == id_cliente_canc).delete_instance()
                self.tab_clienti.removeRow(self.tab_clienti.currentRow())
    
    def deduci_SO(self):
        try:
            ultimo_prev = model_to_dict(Preventivo.select()
                                    .where(Preventivo.anno == self.current_prev["anno"])
                                    .order_by(Preventivo.so.desc())
                                    .get())
        except:
            ultimo_prev = None
        if ultimo_prev == None:
            self.current_prev["so"] = 1
        else:
            self.current_prev["so"] = ultimo_prev["so"] + 1
        self.current_prev["po"] = 0
        self.edit_so.setText(str(self.current_prev["so"]) + "/" + str(self.current_prev["anno"]))
    
    def deduci_PO(self):
        try:
            ultimo_prev = model_to_dict(Preventivo.select()
                                    .where(Preventivo.anno == self.current_prev["anno"])
                                    .order_by(Preventivo.po.desc())
                                    .get())
        except:
            ultimo_prev = None
        if ultimo_prev == None:
            self.current_prev["po"] = 1
        else:
            self.current_prev["po"] = ultimo_prev["po"] + 1
        self.current_prev["so"] = 0
        self.edit_po.setText(str(self.current_prev["po"]) + "/" + str(self.current_prev["anno"]))
    
    def deduci_data(self):
        self.current_prev["data"] = date.today().strftime("%Y-%m-%d")
        self.current_prev["anno"] = date.today().year
        self.edit_data_prev.setDate(QtCore.QDate.fromString(self.current_prev["data"], 'yyyy-MM-dd'))
    
    def scegli_testo_in(self):
        self.quale_testo = "in"
        dialog = DialogScegliTesto()
        if dialog.exec_() != 0:
            testo_da_passare = dialog.testo_da_passare
            self.current_prev["testo_in"] = testo_da_passare
            if len(testo_da_passare) > 50:
                testo_da_passare = testo_da_passare[:45] + "..." # elisione
            self.edit_testo_in.setText(testo_da_passare)

    def scegli_testo_fin(self):
        self.quale_testo = "fin"
        dialog = DialogScegliTesto()
        if dialog.exec_() != 0:
            testo_da_passare = dialog.testo_da_passare
            self.current_prev["testo_fin"] = testo_da_passare
            if len(testo_da_passare) > 50:
                testo_da_passare = testo_da_passare[:45] + "..."
            self.edit_testo_fin.setText(testo_da_passare)

    def deduci_testo_in(self):
        try:
            ultimo_prev = model_to_dict(Preventivo.select()
                                    .where(Preventivo.anno == self.current_prev["anno"])
                                    .order_by(Preventivo.data.desc())
                                    .get())
        except:
            ultimo_prev = None
        if ultimo_prev == None:
            testo_da_passare = ""
        else:
            testo_da_passare = ultimo_prev["testo_in"]
            self.current_prev["testo_in"] = testo_da_passare
        if len(testo_da_passare) > 50:
            testo_da_passare = testo_da_passare[:45] + "..."
        self.edit_testo_in.setText(testo_da_passare)

    def deduci_testo_fin(self):
        try:
            ultimo_prev = model_to_dict(Preventivo.select()
                                    .where(Preventivo.anno == self.current_prev["anno"])
                                    .order_by(Preventivo.data.desc())
                                    .get())
        except:
            ultimo_prev = None
        if ultimo_prev == None:
            testo_da_passare = ""
        else:
            testo_da_passare = ultimo_prev["testo_fin"]
            self.current_prev["testo_fin"] = testo_da_passare
        if len(testo_da_passare) > 50:
            testo_da_passare = testo_da_passare[:45] + "..."
        self.edit_testo_in.setText(testo_da_passare)
        
    def deduci_nick_cliente(self):
        self.current_prev["nick_cliente"] = self.current_cliente["nome"] + " " + self.current_cliente["cognome"]
        self.edit_nick_cliente.setText(self.current_prev["nick_cliente"])

    def crea_prev(self):
        if self.tab_clienti.currentRow() == -1:
            self.popup_nessun_cliente()
        else:
            id_cliente = self.tab_clienti.item(self.tab_clienti.currentRow(), 0).text()
            self.current_cliente = model_to_dict(Cliente.get(Cliente.id == id_cliente))
            self.current_prev["cliente"] = self.current_cliente["id"]
            self.deduci_SO()
            self.deduci_PO()
            self.deduci_data()
            self.load_prev(self.current_prev, self.current_cliente)
    
    def load_prev(self, prev, cliente):
        self.stackedWidget.setCurrentIndex(2)
        self.edit_po.setText("/".join((str(prev["po"]), str(prev["anno"]))))
        self.edit_so.setText("/".join((str(prev["so"]), str(prev["anno"]))))
        self.edit_data_prev.setDate(QtCore.QDate.fromString(prev["data"], 'yyyy-MM-dd'))
        self.edit_nick_cliente.setText(prev["nick_cliente"])
        self.line_prev_nome.setText(cliente["nome"] + " " + cliente["cognome"])
        self.line_prev_via.setText(cliente["via"])
        self.line_prev_cantiere.setText(cliente["cantiere"])
        self.line_prev_comune.setText(cliente["comune"])
        self.line_prev_tel1.setText(cliente["tel1"])
        self.line_prev_tel2.setText(cliente["tel2"])
        self.line_prev_email.setText(cliente["email"])

        if prev["iva"] == int(prev["iva"]):
            self.line_iva.setText(str(int(prev["iva"])))
        else:
            self.line_iva.setText(str(prev["iva"]).replace(".", ","))

        self.listwidget_infissi.clear()
        self.lista_infissi = []
        query = Infisso.select().where(Infisso.prev == prev["id"])
        if query.dicts() != None:
            for num_riga, inf in enumerate(query.dicts()):
                self.lista_infissi.append(inf)
                if inf["posizione"] != ("" or None):
                    posiz = " - %s" %(inf["posizione"].upper())
                self.listwidget_infissi.addItem("SERRAMENTO %d [%s]%s" %(num_riga, inf["codice"], posiz))
                # aggiunta pixmap e thumbnail a ogni riga
        self.view_db_progetti()

    def popola_tree(self, nodo_padre, figlio):
        nodo_figlio_1 = TreeItem(figlio.codice, 12, color = QtGui.QColor(100, 0, 0))
        nodo_figlio_2 = TreeItem(figlio.descriz, 12, color = QtGui.QColor(0, 0, 0))
        nodo_padre.appendRow([nodo_figlio_1, nodo_figlio_2])
        if figlio.figli.dicts() != None:
            for nipote in figlio.figli:
                self.popola_tree(nodo_figlio_1, nipote)
    
    def view_db_progetti(self):
        query = Progetto.select()
        casi_base = query.where(Progetto.genitore == None)
        if casi_base.dicts() != None:
            for caso_base in casi_base:
                self.popola_tree(self.root_node, caso_base)

    def load_progetto_da_edit(self):
        codice_inserito = self.edit_cod_prog.text()
        progetto = Progetto.get_or_none(Progetto.codice == codice_inserito)
        if progetto != None:
            self.edit_descriz.setPlainText(progetto.descriz)
            # mostrare foto 2d e 3d
            self.combo_materiale.clear()
            self.combo_materiale.addItems(";".split(progetto.materiali))
            self.combo_materiale.setCurrentIndex(0)
            self.combo_vernice.clear()
            self.combo_vernice.addItems(";".split(progetto.vernici))
            self.combo_vernice.setCurrentIndex(0)
            
            self.lista_infissi[self.current_index]["cod_prog"] = progetto.codice
            self.lista_infissi[self.current_index]["descriz"] = progetto.descriz
            self.lista_infissi[self.current_index]["materiale"] = self.combo_materiale.itemText(0)
            self.lista_infissi[self.current_index]["vernice"] = self.combo_vernice.itemText(0)
            self.lista_infissi[self.current_index]["foto_2d"] = progetto.foto_2d
            self.lista_infissi[self.current_index]["foto_3d"] = progetto.foto_3d

    def scegli_progetto(self):
        pass # si appoggerà a load_progetto_da_edit

    def deduci_descr(self):
        codice_inserito = self.edit_cod_prog.text()
        progetto = Progetto.get_or_none(Progetto.codice == codice_inserito)
        if progetto != None:
            self.lista_infissi[self.current_index]["descriz"] = progetto.descriz
            self.edit_descriz.setPlainText(progetto.descriz)

    def calc_dim_superf(self):
        inf = self.lista_infissi[self.current_index] # caricamento in memoria per semplicità
        self.line_dimensioni.setHtml(str(inf["lunghezza"] / 10) + " x " + str(inf["altezza"] / 10) + " cm")
        self.line_superficie.setHtml(str(inf["lunghezza"] * inf["altezza"] / 100) + " cm<sup>2</sup>")

    def calc_prezzo_listino(self):
        pass
    
    def tgl_prezzo_listino(self):
        self.edit_prezzo_listino.setEnabled(True)
        prezzo_listino = self.lista_infissi[self.current_index]["prezzo_listino"]
        self.edit_prezzo_listino.setText(str(prezzo_listino.replace(".", ",")))
        self.label_x_1.setEnabled(True)
        self.line_num_pz_1.setEnabled(True)
        self.edit_prezzo_custom.setEnabled(False)
        # self.edit_prezzo_custom.setText("0") # questo deve avvenire dietro le quinte sul database
        self.label_x_2.setEnabled(False)
        self.line_num_pz_2.setEnabled(False)

    def tgl_prezzo_custom(self):
        self.edit_prezzo_listino.setEnabled(False)
        # self.edit_prezzo_listino.setText("0")  # questo deve avvenire dietro le quinte sul database
        self.label_x_1.setEnabled(False)
        self.line_num_pz_1.setEnabled(False)
        self.edit_prezzo_custom.setEnabled(True)
        prezzo_custom = self.lista_infissi[self.current_index]["prezzo_custom"]
        self.edit_prezzo_custom.setText(str(prezzo_custom.replace(".", ",")))
        self.label_x_2.setEnabled(True)
        self.line_num_pz_2.setEnabled(True)

    def tgl_sconto(self):
        self.edit_sconto.setEnabled(True)
        pass # wip

    def tgl_sconto_percent(self):
        pass

    def calc_importo_netto(self):
        current_inf = self.lista_infissi[self.current_index]
        if current_inf["prezzo_listino"] > 0:
            self.edit_importo_netto.setText(str(current_inf["prezzo_listino"] * current_inf["num_pz"]))
        else:
            self.edit_importo_netto.setText(str(current_inf["prezzo_custom"] * current_inf["num_pz"]))

    def calc_importo_lordo(self):
        current_inf = self.lista_infissi[self.current_index]
        if current_inf["prezzo_listino"] > 0:
            prezzo = current_inf["prezzo_listino"] * current_inf["num_pz"]
        else:
            prezzo = current_inf["prezzo_custom"] * current_inf["num_pz"]
        if current_inf["sconto"] > 1:
            prezzo -= current_inf["sconto"]
        else:
            prezzo -= prezzo * current_inf["sconto"]
        prezzo += prezzo * self.current_prev["iva"]
        self.line_importo_lordo.setText(str(prezzo))

    def load_infisso(self):
        self.current_index = self.listwidget_infissi.currentRow()
        current_inf = self.lista_infissi[self.current_index]
        self.edit_cod_prog.setText(current_inf["cod_prog"])
        self.edit_posiz.setText(current_inf["posiz"])
        self.edit_descriz.setPlainText(current_inf["descriz"])
        self.edit_note_descriz.setText(current_inf["note_descriz"])
        # caricare foto 2d e 3d

        self.spin_num_pz.setValue(current_inf["num_pz"])
        self.line_num_pz_1.setText(str(current_inf["num_pz"]))
        self.line_num_pz_2.setText(str(current_inf["num_pz"]))
        self.spin_lunghezza.setValue(current_inf["lunghezza"])
        self.spin_altezza.setValue(current_inf["altezza"])
        self.combo_materiale.setCurrentIndex(self.combo_materiale.findText(current_inf["materiale"]))
        self.combo_vernice.setCurrentIndex(self.combo_vernice.findText(current_inf["materiale"]))
        self.edit_note_varianti.setPlainText(current_inf["note_varianti"])
        self.calc_dim_superf()

        if current_inf["prezzo_listino"] > 0:
            self.radio_prezzo_listino.toggle()
        else:
            self.radio_prezzo_custom.toggle()       
        if current_inf["sconto"] > 1:
            self.radio_sconto.toggle()
        else:
            self.radio_sconto_percent.toggle()
        self.calc_importo() 

    def salva_prev(self):
        self.popup_salva_prev()



    def closeEvent(self, event): # override per non chiudere la finestra senza salvare
        if self.safe_exit:
            event.accept()
        else: # sostituire questo layout con un popup
            reply = QtWidgets.QMessageBox.question(self, 'Chiusura della finestra di lavoro', 'Chiudendo la finestra di lavoro adesso si perderanno tutti i progressi. Chiudere la finestra?',
                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

            if reply == QtWidgets.QMessageBox.Yes:
                event.accept()
                print('Window closed')
            else:
                event.ignore()

    # <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> <> #
            
### ALLA FINE

    import sys
    app = QtWidgets.QApplication(sys.argv)
    reGI = QtWidgets.QMainWindow()
    reGI.setWindowTitle("reGI a0.3.X")
    reGI.setWindowIcon(QtGui.QIcon("../Risorse/icon_0.png"))
    ui = Ui_reGI()
    ui.setupUi(reGI)
    reGI.show()
    sys.exit(app.exec_())
    db.close()

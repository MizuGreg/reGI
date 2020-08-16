### ALL'INIZIO

from PyQt5 import QtCore, QtGui, QtWidgets

import sentry_sdk
sentry_sdk.init("https://d770165f943e497484a6fa95ebcef724@o429982.ingest.sentry.io/5377715")
from regi_db import db, Value, Cliente, Preventivo, TestoIn, TestoFin, Progetto, Infisso
from regi_db import model_to_dict
from datetime import date

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
            self.cliente_nuovo = {"cognome": self.edit_cognome.text(), # attenzione, niente ID!
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
            self.cliente_modificato = {"cognome": self.edit_cognome.text(), # attenzione, niente ID!
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
        self.setWindowTitle("Scegli il testo iniziale/finale")
        self.resize(700, 500)
        self.centralWidget = QtWidgets.QWidget()
        self.btn_aggiungi = QtWidgets.QPushButton(self.centralWidget)
        self.btn_aggiungi.setGeometry(QtCore.QRect(10, 450, 80, 41))
        self.btn_aggiungi.setText("Aggiungi")
        self.btn_modifica = QtWidgets.QPushButton(self.centralWidget)
        self.btn_modifica.setGeometry(QtCore.QRect(100, 450, 80, 41))
        self.btn_modifica.setText("btn_modifica")
        self.btn_elimina = QtWidgets.QPushButton(self.centralWidget)
        self.btn_elimina.setGeometry(QtCore.QRect(190, 450, 80, 41))
        self.btn_elimina.setText("btn_elimina")
        self.btn_scegli = QtWidgets.QPushButton(self.centralWidget)
        self.btn_scegli.setGeometry(QtCore.QRect(610, 450, 80, 41))
        self.btn_scegli.setText("btn_scegli")
        self.edit_testo_selez = QtWidgets.QTextEdit(self.centralWidget)
        self.edit_testo_selez.setEnabled(True)
        self.edit_testo_selez.setGeometry(QtCore.QRect(10, 320, 581, 111))
        self.edit_testo_selez.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.edit_testo_selez.setReadOnly(True)
        self.tab_testi = QtWidgets.QTableWidget(self.centralWidget)
        self.tab_testi.setGeometry(QtCore.QRect(10, 10, 681, 301))
        self.tab_testi.setColumnCount(2)
        self.tab_testi.setRowCount(0)
        self.tab_testi.setHorizontalHeaderLabels("ID", "Testo")
        self.tab_testi.horizontalHeader(self.centralWidget).setStretchLastSection(True)
        self.btn_fatto = QtWidgets.QPushButton(self.centralWidget)
        self.btn_fatto.setGeometry(QtCore.QRect(610, 350, 80, 41))
        self.btn_fatto.setText("Fatto")

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
        pass

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
        
        elif self.operazione == "modifica":
            num_riga = self.tab_testi.currentRow()
            id_testo_modificato = self.tab_testi.item(num_riga, 0).text()
            testo_modificato = self.edit_testo_selez.toPlainText()
            if ui.quale_testo == "in":
                query = TestoIn.update(testo_modificato).where(TestoIn.id == id_testo_modificato)
            else:
                query = TestoFin.update(testo_modificato).where(TestoFin.id == id_testo_modificato)
            query.execute()
            # wip
        
        self.operazione = ""
        self.edit_testo_selez.setReadOnly(True)
        self.edit_testo_selez.setFrameShape(QtWidgets.QFrame.NoFrame)

    def scegli(self):
        pass

### IN QUESTO ORDINE

    ###

        self.stackedWidget.setCurrentIndex(0)
        self.current_cliente = {"id": 0, "cognome": "", "nome": "", "via": "", "comune": "", "tel1": "", "tel2": "", "email": "", "cantiere": ""}
        self.current_prev = {"id": 0, "cliente": 0, "nick_cliente": "", "anno": 0, "so": 0, "po": 0, "data": "", "testo_in": "", "testo_out": ""}
        self.current_infisso = {"id": 0, "prev": 0, "cod_prog": 0, "posizione": "", "descrizione": "", "note": "", "num_pz": 0, "lunghezza": 0,
                                "altezza": 0, "spessore": 0, "materiale": "", "vernice": "", "var3": "", "note_varianti": "", "prezzo_netto": 0,
                                "sconto": 0, "iva": 0, "prezzo_lordo": 0}
        self.btn_nuovo_prev.clicked.connect(self.view_db_clienti)
        self.btn_view_anagrafica.clicked.connect(self.view_anagrafica)
        self.btn_sc_agg_cliente.clicked.connect(self.sc_agg_cliente)
        self.btn_sc_edit_cliente.clicked.connect(self.sc_edit_cliente)
        self.btn_scegli_cliente.clicked.connect(self.crea_prev)
        self.btn_agg_cliente.clicked.connect(self.agg_cliente)
        self.btn_edit_cliente.clicked.connect(self.edit_cliente)
        self.btn_canc_cliente.clicked.connect(self.canc_cliente)

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
        if dialog.exec_() != 0: # .reject() dà 0, quindi questa parte corrisponde a .accept()
            cliente_nuovo = dialog.cliente_nuovo
            # c = Cliente.create(cliente_nuovo)
            c = Cliente.create( # id = None,
                                cognome = cliente_nuovo["cognome"],
                                nome = cliente_nuovo["nome"],
                                via = cliente_nuovo["via"],
                                comune = cliente_nuovo["comune"],
                                tel1 = cliente_nuovo["tel1"],
                                tel2 = cliente_nuovo["tel2"],
                                email = cliente_nuovo["email"],
                                cantiere = cliente_nuovo["cantiere"])
            c = model_to_dict(c)
            num_riga = self.tab_clienti.rowCount()
            self.tab_clienti.insertRow(num_riga) 
            for num_colonna, dato in enumerate(c.values()): # carica il cliente
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
                c = Cliente.get(Cliente.id == id_cliente_edit)
                c = model_to_dict(c)
                for num_colonna, dato in enumerate(c.values()): # ricarica il cliente
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
            if len(testo_da_passare) > 50:
                testo_da_passare = testo_da_passare[:45] + "..." # elisione
            self.edit_testo_in.setText(testo_da_passare)

    def scegli_testo_fin(self):
        self.quale_testo = "fin"
        dialog = DialogScegliTesto()
        if dialog.exec_() != 0:
            testo_da_passare = dialog.testo_da_passare
            if len(testo_da_passare) > 50:
                testo_da_passare = testo_da_passare[:45] + "..." # elisione
            self.edit_testo_fin.setText(testo_da_passare)

    def deduci_testo_in(self):
        try:
            ultimo_prev = model_to_dict(Preventivo.select()
                                    .where(Preventivo.anno == self.current_prev["anno"])
                                    .get())
        except:
            ultimo_prev = None
        if ultimo_prev == None:
            self.current_prev["testo_in"] = ""
        else:
            self.current_prev["testo_in"] = ultimo_prev["testo_in"]
        self.edit_testo_in.setText(self.current_prev["testo_in"])

    def deduci_testo_fin(self):
        try:
            ultimo_prev = model_to_dict(Preventivo.select()
                                    .where(Preventivo.anno == self.current_prev["anno"])
                                    .get())
        except:
            ultimo_prev = None
        if ultimo_prev == None:
            self.current_prev["testo_fin"] = ""
        else:
            self.current_prev["testo_fin"] = ultimo_prev["testo_fin"]
        self.edit_testo_fin.setText(self.current_prev["testo_fin"])

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
        self.edit_nome_cliente.setText(prev["nick_cliente"])
        self.line_prev_nome.setText(" ".join((cliente["nome"], cliente["cognome"])))
        self.line_prev_via.setText(cliente["via"])
        self.line_prev_cantiere.setText(cliente["cantiere"])
        self.line_prev_comune.setText(cliente["comune"])
        self.line_prev_tel1.setText(cliente["tel1"])
        self.line_prev_tel2.setText(cliente["tel2"])
        self.line_prev_email.setText(cliente["email"])
        
        # loading degli infissi

    
    ###
            
### ALLA FINE

    import sys
    app = QtWidgets.QApplication(sys.argv)
    reGI = QtWidgets.QMainWindow()
    reGI.setWindowTitle("reGI a0.3.X")
    reGI.setWindowIcon(QtGui.QIcon("../Icone/icon_0.png"))
    ui = Ui_reGI()
    ui.setupUi(reGI)
    reGI.show()
    sys.exit(app.exec_())
    db.close()

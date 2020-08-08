"""
Script Python che genera il db, lo costruisce ad hoc
e apre la connessione (ma non la chiude). Viene chiamato dallo script principale.
"""
import os
import sys
from peewee import SqliteDatabase, Model, AutoField, CharField, IntegerField, ForeignKeyField, TextField, DateField
from playhouse.shortcuts import model_to_dict
from datetime import date

db = SqliteDatabase('regidb_0.db')

class Cliente(Model):
    """
    Questa è una tabella del database, quella che si occupa dei clienti.
    cognome, nome ecc. sono le colonne della tabella.
    null=True vuol dire che sono accettati campi vuoti.
    la classe Meta indica che regidb_0.db viene usato come database.
    """
    id = AutoField()
    cognome = CharField() # colonne della tabella
    nome = CharField()
    via = CharField(null = True) # vuol dire che posso lasciare il campo vuoto
    comune = CharField(null = True)
    tel1 = CharField(null = True)
    tel2 = CharField(null = True)
    email = CharField(null = True)
    cantiere = CharField(null = True)
    class Meta:
        database = db # questo vuol dire che questo modello usa "regidb_0.db" come database

class Preventivo(Model):
    """
    Questa tabella del database si occupa dei preventivi.
    L'attributo lista_inf è una lista che contiene gli infissi
    del preventivo.
    """
    id = AutoField()
    cliente = ForeignKeyField(Cliente, backref = "preventivi")
    nick_cliente = CharField(null = True)
    anno = IntegerField(null = True, default = date.today().year)
    so = IntegerField(null = True)
    po = IntegerField(null = True)
    data = CharField(null = True)
    # key_testo_in = ForeignKeyField(Testo, null = True)
    testo_in = CharField(null = True) # TextField?
    # key_testo_out = ForeignKeyField(Testo, null = True)
    testo_out = CharField(null = True) # TextField?
    class Meta:
        database = db

class Testo(Model):
    """
    Tabella che registra i testi iniziali e finali da
    inserire nei preventivi.
    """
    id = AutoField()
    testo = CharField(null = True) # TextField?
    class Meta:
        database = db

class Progetto(Model):
    """
    Tabella che registra i progetti per gli infissi.
    """
    codice = CharField(unique = True, primary_key = True)
    descrizione = CharField(null = True) # TextField?
    foto_2d = CharField(null = True)
    foto_3d = CharField(null = True)
    materiali = CharField(null = True) # lista dei materiali consentiti
    vernici = CharField(null = True)

    class Meta:
        database = db

class Infisso(Model):
    """
    Classe che genera la voce Infisso, che ha alcuni attributi.
    """
    id = AutoField()
    prev = ForeignKeyField(Preventivo, backref = "infissi")
    cod_prog = ForeignKeyField(Progetto)
    posizione = CharField(null = True)
    descrizione = CharField(null = True) # TextField?
    note = CharField(null = True)
    num_pz = IntegerField(null = True)
    lunghezza = IntegerField(null = True)
    altezza = IntegerField(null = True)
    spessore = IntegerField(null = True)
    materiale = CharField(null = True)
    vernice = CharField(null = True)
    var3 = CharField(null = True)
    note_varianti = CharField(null = True)
    prezzo_netto = IntegerField(null = True)
    sconto = IntegerField(null = True)
    iva = IntegerField(null = True)
    prezzo_lordo = IntegerField(null = True)
    class Meta:
        database = db

db.connect()
db.create_tables([Cliente, Preventivo, Testo, Progetto])

# queste righe servono solo per riempire il DB e testarne il funzionamento
cliente_prova = Cliente(cognome="Dimaglie", nome="Gregorio", via="via C. Golgi, 33", comune="Manduria (TA)")
prev_prova = Preventivo(cliente=cliente_prova, num_progr="2/2020")
cliente_prova.save()
prev_prova.save()

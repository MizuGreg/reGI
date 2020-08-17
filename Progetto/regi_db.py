"""
Script Python che genera il db, lo costruisce ad hoc
e apre la connessione con il db (ma non la chiude).
Viene chiamato dallo script principale.
Tutti i parametri null = True dovranno diventare obsoleti.
"""
import os
import sys
from peewee import SqliteDatabase, Model, Value, AutoField, CharField, IntegerField, ForeignKeyField, TextField, FloatField
from playhouse.shortcuts import model_to_dict
from datetime import date

db = SqliteDatabase('regidb_0.db')

class BaseModel(Model):
    """
    Tabella base del database. La classe Meta indica che regidb_0.db
    viene usato come database.
    """
    class Meta:
        database = db

class Cliente(BaseModel):
    """
    Tabella del database che si occupa dei clienti.
    cognome, nome ecc. sono le colonne della tabella.
    null = True vuol dire che sono accettati campi vuoti.
    """
    id = AutoField()
    cognome = CharField()
    nome = CharField()
    via = CharField(null = True)
    comune = CharField(null = True)
    tel1 = CharField(null = True)
    tel2 = CharField(null = True)
    email = CharField(null = True)
    cantiere = CharField(null = True)

class Preventivo(BaseModel):
    """
    Tabella del database che custodisce tutti i preventivi.
    cliente è una foreign key che punta alla tabella Cliente.
    """
    id = AutoField()
    cliente = ForeignKeyField(Cliente, backref = "preventivi")
    nick_cliente = CharField(null = True)
    anno = IntegerField(null = True) # default = date.today().year)
    so = IntegerField(null = True)
    po = IntegerField(null = True)
    data = CharField(null = True) # default = date.today().strftime("%Y-%m-%d"))
    # key_testo_in = ForeignKeyField(Testo, null = True)
    testo_in = TextField(null = True)
    # key_testo_out = ForeignKeyField(Testo, null = True)
    testo_fin = TextField(null = True)

class TestoIn(BaseModel):
    """
    Tabella che registra solo i testi iniziali da inserire
    nei preventivi.
    """
    id = AutoField()
    testo = TextField(null = True)

class TestoFin(BaseModel):
    """
    Tabella che registra solo i testi finali da inserire
    nei preventivi.
    """
    id = AutoField()
    testo = TextField(null = True)

class Progetto(BaseModel):
    """
    Tabella che registra i progetti base da cui partire
    per costruire gli infissi.
    """
    codice = CharField(unique = True, primary_key = True)
    genitore = ForeignKeyField("self", null = True, backref = "figli")
    nome = CharField(null = True)
    descrizione = TextField(null = True)
    foto_2d = TextField(null = True)
    foto_3d = TextField(null = True)
    materiali = CharField(null = True) # lista dei materiali consentiti. Usare "; ".split()
    vernici = CharField(null = True)

class Infisso(BaseModel):
    """
    Classe che genera la voce Infisso, che ha alcuni attributi.
    """
    id = AutoField()
    prev = ForeignKeyField(Preventivo, backref = "infissi")
    cod_prog = ForeignKeyField(Progetto)
    posizione = CharField(null = True)
    descrizione = TextField(null = True)
    note = CharField(null = True)
    num_pz = IntegerField(null = True)
    lunghezza = IntegerField(null = True)
    altezza = IntegerField(null = True)
    spessore = IntegerField(null = True)
    materiale = CharField(null = True)
    vernice = CharField(null = True)
    note_varianti = CharField(null = True)
    prezzo_netto = IntegerField(null = True)
    sconto = FloatField(null = True)

db.connect()
db.create_tables([Cliente, Preventivo, TestoIn, TestoFin, Progetto, Infisso])

# Queste righe servono solo per riempire il DB e testarne il funzionamento.

def popola_clienti():
    Cliente.create(cognome = "Dimaglie", nome = "Gregorio",
                                via = "via C. Golgi, 33", comune = "Manduria (TA)",
                                tel1 = "3294633960")

def popola_preventivi():
    pass

def popola_progetti():
    Progetto.create(codice = "BA", genitore = None, nome = "Sistema base", descrizione = "")
    Progetto.create(codice = "AS", genitore = "BA", nome = "Alzante scorrevole", descrizione = "")
    Progetto.create(codice = "HS5--------------------------------------------------", genitore = "AS", nome = "Alzante scorrevole 5 ante", descrizione = "Alzante scorrevole a cinque ante.---------------------------------------------------------")
    Progetto.create(codice = "LA", genitore = None, nome = "Legno/alluminio", descrizione = "")

popola_clienti()
popola_preventivi()
# popola_progetti()

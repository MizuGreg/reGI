"""
Esperimento atto SOLAMENTE a verificare il funzionamento del database.
"""
import os
import sys
import time
from peewee import * # include sqlite3
from PyQt5 import QtGui #boh
from PyQt5.QtWidgets import * #boh
from PyQt5.QtGui import QIcon #boh
from PyQt5.QtCore import * #boh
from datetime import date

db = SqliteDatabase('db-regi--1.db')

class Cliente(Model): # tabella
    cognome = CharField() # colonne della tabella
    nome = CharField()
    via = CharField(null=True) # vuol dire che posso lasciare il campo vuoto
    comune = CharField(null=True)
    num1 = CharField(null=True)
    num2 = CharField(null=True)
    email = CharField(null=True)
    cantiere = CharField(null=True)
    class Meta: # non so cosa voglia dire: istanze (righe) della tabella
        database = db # questo vuol dire che questo modello usa "db-regi--1.db" come database
class Preventivo(Model):
    cliente = ForeignKeyField(Cliente, backref="preventivi")
    num_prog = CharField(null=True)
    data = DateField(null=True)

    class Meta:
        database = db
# la classe Infisso avrà attributi nome, lunghezza, altezza, prezzo, variante1, variante2

db.connect()
db.create_tables([Cliente, Preventivo])
db.close()
try:
    os.remove("db-regi--1.db") ### ATTENZIONE è UNA PRECAUZIONE DOVUTA AL CARATTERE SPERIMENTALE
    ### DI QUESTO SCRIPT PYTHON!!! ###
except Exception as e:
    print(e)

"""
Script Python che genera il db, lo costruisce ad hoc
e apre la connessione (ma non la chiude). Viene chiamato dallo script principale.
"""
import os
import sys
from peewee import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from datetime import date

db = SqliteDatabase('regidb_0.db')

class Cliente(Model):
    """
    Questa è una tabella del database, quella che si occupa dei clienti.
    cognome, nome ecc. sono le colonne della tabella.
    null=True vuol dire che sono accettati campi vuoti.
    la classe Meta indica che regidb_0.db viene usato come database.
    """
    cognome = CharField() # colonne della tabella
    nome = CharField()
    via = CharField(null=True) # vuol dire che posso lasciare il campo vuoto
    comune = CharField(null=True)
    num1 = CharField(null=True)
    num2 = CharField(null=True)
    email = CharField(null=True)
    cantiere = CharField(null=True)
    class Meta:
        database = db # questo vuol dire che questo modello usa "regidb_0.db" come database
class Preventivo(Model):
    """
    Questa tabella del database si occupa dei preventivi.
    E' in realtà ibrida, perché contiene anche attributi
    tipici della OOP e non dei DB (cioè lista_inf).
    """
    cliente = ForeignKeyField(Cliente, backref="preventivi")
    num_prog = CharField(null=True)
    data = DateField(null=True)
    lista_inf = []
    class Meta:
        database = db
class Infisso():
    """
    Classe che genera l'oggetto Infisso, che ha alcuni attributi.
    L'oggetto/dato Preventivo conterrà, nella lista lista_inf, gli infissi
    preventivati e aggiornerà il totale di conseguenza.
    """
    def __init__(self, **kwargs):
        self.codice = kwargs.get('codice', "")
        self.lunghezza = kwargs.get('lunghezza', 0)
        self.altezza = kwargs.get("altezza", 0)
        self.prezzo = kwargs.get("prezzo", 0)
        self.var1 = kwargs.get("var1", "")
        self.var2 = kwargs.get("var2", "")

db.connect()
db.create_tables([Cliente, Preventivo])

### queste righe servono solo per riempire il DB e testarne il funzionamento
cliente0 = Cliente(cognome="Dimaglie", nome="Gregorio", via="via C. Golgi, 33", comune="Manduria (TA)")
prev0 = Preventivo(cliente=cliente0, num_prog="1/2019")
inf0 = Infisso(codice="PF2", lunghezza=2000, altezza=2500)
prev0.lista_inf.append(inf0)
cliente0.save()
prev0.save()
for prev in Preventivo.select():
    for inf in prev.lista_inf:
        print(str(inf.lunghezza))

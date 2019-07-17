"""
Esperimento atto a definire l'oggetto Infisso e come interagisce con l'oggetto Preventivo
nel database di reGI. Questo file .py si occupa della definizione della classe Infisso.
"""
import esp_db
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
esp_db.db.connect()
cliente0 = esp_db.Cliente(cognome="Dimaglie", nome="Gregorio")
prev0 = esp_db.Preventivo(cliente=cliente0, num_prog="1/2019")
# finché non eseguo cliente0.save() o prev0.save() non fanno parte del db!
inf0 = Infisso(codice="PF2", lunghezza=2300, altezza=2400)
prev0.lista_inf.append(inf0)
cliente0.save()
prev0.save()
for prev in esp_db.Preventivo.select():
    for inf in prev.lista_inf:
        print(str(inf.lunghezza))
# it works just fine!

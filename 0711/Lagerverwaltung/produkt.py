class Produkt:
    def __init__(self, name, produkt_id, preis, bestand):
        self.name = name
        self.produkt_id = produkt_id
        self.preis = preis 
        self.bestand = bestand
    def anzeigen_details(self):
        '''soll alle Details des Produkts 
        (Name, ID, Preis, Bestand) 
        in einem gut lesbaren
        Format auf der Konsole ausgeben.'''
        return f"Produkt: {self.name} (ID: {self.produkt_id})\nPreis: {self.preis}\nVerfügbar: {self.bestand}"

    def produkt_verkaufen(self, menge):
        '''Die Methode soll den bestand des Produkts
        um die verkaufte Menge reduzieren.'''
        if menge <= self.bestand:
            self.bestand -=  menge
            return f"neue Bestand {self.bestand} nach verkauf"
        else:
            #print(f"Nicht genügend {self.name} auf Lager, verfügbar: {self.bestand}, versucht zu verkaufen: {menge}")
            return f"Nichr genügend {self.name} auf Lager, verfügbar: {self.bestand}, versucht zu verkaufen: {menge}"

    def bestand_auffuellen(self, menge):
        '''Die Methode soll den bestand des Produkts
        um die angegebene Menge erhöhen.'''
        self.bestand += menge

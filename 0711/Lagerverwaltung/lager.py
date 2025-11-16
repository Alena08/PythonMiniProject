class Lager:
    def __init__(self):
        #self.name = name
        self.produkte =[]
    def produkt_hinzufuegen(self, produkt):
        self.produkte.append(produkt)

    def alle_produkte_anzeigen(self):
        return  [produkt.anzeigen_details() for produkt in self.produkte]
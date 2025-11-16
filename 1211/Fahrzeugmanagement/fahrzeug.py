class Fahrzeug:
    anzahl_fahrzeuge = 0
    def __init__(self, marke, geschwindigkeit=0):
        self.__marke = marke
        self.__geschwindigkeit = geschwindigkeit
        Fahrzeug.anzahl_fahrzeuge += 1

    def beschleunigen(self):
        return self.__geschwindigkeit + 10
    
    @classmethod
    def gesamtbestand_pruefen(cls):
        return cls.anzahl_fahrzeuge
    
    @property
    def geschwindigkeit(self):
        return self.__geschwindigkeit
    
    @geschwindigkeit.setter
    def geschwindigkeit(self, nue):
        self.__geschwindigkeit = nue
    
    @property 
    def marke(self):
        return self.__marke
    
    @marke.setter
    def marke(self, neue_marke):
        self.__marke = neue_marke
        
        
class Fahrzeug:
    def __init__(self, marke:str, modell:str, baujahr:int, farbe:str):
        self.__marke = marke
        self.__modell = modell
        self.__baujahr = baujahr
        self.__farbe = farbe
        self.__motorGestartet = False
    def getMarke(self):
        return self.__marke
    def getModell(self):
        return self.__modell
    def getBaujahr(self):
        return self.__baujahr
    def getFarbe(self):
        return self.__farbe
    def getMotor(self):
        return self.__motorGestartet
    
    def setFarbe(self, neufarbe):
        self.__farbe = neufarbe
    
    def setBaujahr(self, jahr):
        self.__baujahr = jahr

    def starten(self):
        self.__motorGestartet = True
        return f"Der Motor des {self.getMarke()} {self.getModell()}wurde gestartet."
    def ausschalten(self):
        self.__motorGestartet = False
        return f"Der Motor des {self.getMarke()} {self.getModell()}wurde ausgeschaltet."
    
    def informationAusgaben(self):
        return f"das Auto {self.getMarke()} {self.getModell()} \nBaujahr: {self.getBaujahr()}\nFarbe: {self.getFarbe()}"
    def fahren(self):
        if self.getMotor() == True:
            return "Das Auto fährt"
        else:
            return "das Auto muss erst gestarten werden"
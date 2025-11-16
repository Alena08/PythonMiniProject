from fahrzeug import Fahrzeug

class Auto(Fahrzeug):
    
    def __init__(self, marke, geschwindigkeit, anzahl_tueren):
        super().__init__(marke, geschwindigkeit)
        self.__anzahl_tueren = anzahl_tueren

    #Override
    def beschleunigen(self):
        print("das Auto beschleunigt.")
        self.geschwindigkeit += 20
        return self.geschwindigkeit 
    
    @staticmethod
    def zulassungsinformation():
        return f"Alle Autos benötigen eine gültige Zulassung."
        
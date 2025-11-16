class Mitarbeiter:
    ERHOEHUNGSRATE = 1.05
    def __init__(self, name, gehalt):
        self.name = name
        self.gehalt = gehalt
       
    def erhoehe_gehalt(self):
        return self.gehalt*Mitarbeiter.ERHOEHUNGSRATE
    
    @staticmethod
    def ist_vollzeit(stunden):
        return stunden >= 40        

class Entwickler(Mitarbeiter):
    ERHOEHUNGSRATE = 1.10
    def erhoehe_gehalt(self):
        return self.gehalt*Entwickler.ERHOEHUNGSRATE

m1 = Mitarbeiter("Alena", 3000)
m2 = Mitarbeiter("Tom", 4000)
e1 = Entwickler("Matz", 3000)
print(m1.erhoehe_gehalt())
print(e1.erhoehe_gehalt())
print(m1.gehalt)
print(e1.gehalt)
print(Mitarbeiter.ist_vollzeit(36))
print(Entwickler.ist_vollzeit(40))
class Mitarbeiter:
    # Klassenattribute: Ein Zähler
    __anzahl_mitarbeiter = 0

    def __init__(self, name, gehalt):
        # Instanzattribute
        self.name = name
        self.gehalt = gehalt
        Mitarbeiter.__anzahl_mitarbeiter += 1
    
    def get_Name(self):
        return self.name
    
    # Klassenmethode als getter für klassenattribute
    @classmethod
    def get_anzahl_mitarbeiter(cls):
        return cls.__anzahl_mitarbeiter

    #Klassenmethode als alternativer Konstrukor
    @classmethod
    def aus_csv_string(cls, csv_string):
        """ Erstellt ein Mitarbeiter-Objekt aus einem String wie 'Ali Müller-3000' """
        name, gehalt_str = csv_string.split('-')
        gehalt= int(gehalt_str)

        # Wir rufen den Haupt-Konstruktor __init__ auf
        # indem wir die Klasse selbst(cls) benutzen
        return cls(name,gehalt) # <---- 'cls' ist hier ein Platzhalter für 'Mitarbeiter'

    # Als Hilfsfunktionen oder Utility-Aufgaben
    @staticmethod
    def ist_gehalt_gueltig(gehalt):
        MINDESTLOHN = 12000
        return gehalt >= MINDESTLOHN

# Standard
m1 = Mitarbeiter("Rayen",3000)

# Alternative mit der Klassenmethode
daten_aus_datei = "Ali Müller-5000"
m2 = Mitarbeiter.aus_csv_string(daten_aus_datei)

print(f"Mitarbeiter: {m1.name}, Gehalt: {m1.gehalt}")
print(f"Mitarbeiter: {m2.name}, Gehalt: {m2.gehalt}")
print(f"Gesamtzahl Mitarbeiter {Mitarbeiter.get_anzahl_mitarbeiter()}")

print(Mitarbeiter.ist_gehalt_gueltig(5000))
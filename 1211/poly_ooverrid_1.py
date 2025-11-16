# Klasse
class Tier:
    #Instanzmethode 
    def sprich(self):
        print("Ein Tier macht ein Geräusch")

class Hund(Tier): # Vererbung
    # Methode überschreiben
    def sprich(self):
        print("Wuff!")

class Katze(Tier): # Vererbung
    # Methode überschreiben
    def sprich(self):
        print("Miau!")

# Polymorphismus = Gleiche Schnittstelle, unterschiedlisches Verhalten
# poly = viele , morph= Gestalt/Formen


tiere = [Hund(),Katze(),Tier()]

for t in tiere:
    t.sprich()

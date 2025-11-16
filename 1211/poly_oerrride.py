# Override (Überschreiben) --> methoden , attribute

class Fahrzeug:
    def starten(self):
        print("Das Fahrzeug startet.....")


class Auto(Fahrzeug):
    def starten(self):
        print("Der Motor vom Auto startet.....")

fz = Fahrzeug()
fz.starten()

auto = Auto()
auto.starten()

klasse = 5
maria = klasse

print(klasse)
maria = 6
print(maria)
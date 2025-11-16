from parkplatz import Parkplatz
class Etage:
    """Verwaltet die Parkplätze auf einer Etage."""
    def __init__(self, etagennummer, parkplaetznumber):
        self.etagennummer = etagennummer
        self.parkplaetze = []
        self.configParkplaetze(parkplaetznumber)

    def configParkplaetze(self, parkplaetzenumber):
        """Erstellt Parkplatz-Objekte."""
        self.parkplaetze = [Parkplatz(i) for i in range(1, parkplaetzenumber+1)]

    def freiePlatz(self):
        """Sucht den ersten freien Platz auf der Etage."""
        for platz in self.parkplaetze:
            if not platz.getStatus(): 
                return platz
        return None
    
    def get_freier_platz_anzahl(self) -> int:
        """Gibt die Gesamtzahl der freien Parkplätze auf dieser Etage zurück."""
        return sum(1 for p in self.parkplaetze if not p.getStatus())
    
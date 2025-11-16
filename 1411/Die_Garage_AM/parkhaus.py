from etage import Etage
from parkplatz import Parkplatz
from fahrzeug import Fahrzeug
class Parkhaus:
    """Die Hauptklasse zur Verwaltung des Parkhauses."""
    def __init__(self,anzahl_etagen,parkplases):
        self.etagen = [] 
        self.configEtage(anzahl_etagen, parkplases)

    def configEtage(self, anzahl_etagen, parkplases):
        """Erstellt die Etagen-Objekte."""
        for i in range(1, anzahl_etagen + 1):
            self.etagen.append(Etage(i, parkplases))
        gesamt_plaetze = anzahl_etagen*parkplases
        print(f"Parkhaus mit {anzahl_etagen} Etagen und {gesamt_plaetze} Plätzen initialisiert.")

    def findParklotByCarId(self, carId):
        for e in self.etagen:
            for p in e.parkplaetze:
                if p.parked_fahrzeug != None and p.parked_fahrzeug.id == carId:
                    return e, p

    def parken(self, fahrzeug: Fahrzeug) -> str:
        """Weist einem einfahrenden Fahrzeug einen freien Platz zu."""
        
        # 1. Eindeutigkeitsprüfung
        if self.findParklotByCarId(fahrzeug.id):
            return f"Ablehnung: Fahrzeug {fahrzeug.id} ist bereits im Parkhaus."

        # 2. Platzsuche und Zuweisung 
        for etage in self.etagen:
            freier_platz = etage.freiePlatz() 
            if freier_platz:
                freier_platz.parkCar(fahrzeug)
                return (f"Erlaubt: {fahrzeug} parkt auf Etage {etage.etagennummer}, "
                        f"Parkplatz {freier_platz.nummer}.")
        # 3. Ablehnung
        return f"Ablehnung: Keine freien Plätze vorhanden."
    
    def verlassen(self, fahrzeug_id: str) -> str:
        """Lässt ein Fahrzeug das Parkhaus verlassen und gibt den Platz frei."""
        # 1. Fahrzeug-Ortung und Platz-Freigabe
        if not self.findParklotByCarId(fahrzeug_id):
             return f"Fehler: Fahrzeug mit ID {fahrzeug_id} wurde im Parkhaus nicht gefunden."
        
        # Holt den Parkplatz, den das Fahrzeug belegt hat
        etage, platz = self.findParklotByCarId(fahrzeug_id)
        platz.freigeben()       
        return (f"Erfolg: (ID: {fahrzeug_id}) hat das Parkhaus von Etage "
                f"{etage.etagennummer}, Parkplatz {platz.nummer} verlassen.")

    def get_position(self, fahrzeug_id: str) -> str:
        """Fragt die Position eines bestimmten Fahrzeugs ab."""
        if not self.findParklotByCarId(fahrzeug_id):
            return f"Info: Fahrzeug mit ID {fahrzeug_id} parkt derzeit nicht im Parkhaus."
        etage, platz = self.findParklotByCarId(fahrzeug_id)
        return (f"Position: Fahrzeug {fahrzeug_id} befindet sich auf **Etage {etage.etagennummer}**, "
                f"**Parkplatz {platz.nummer}**.")

    def get_freie_plaetze_anzahl(self) -> str:
        """Gibt die Gesamtanzahl der noch freien Parkplätze zurück."""
        gesamt_freie = 0
        for etage in self.etagen:
            gesamt_freie += etage.get_freier_platz_anzahl()    
        return f"Freie Plätze gesamt: {gesamt_freie}"
    
    def getStatus(self):
        statusString= "------ Parking Garage Status ------\n"
        for etage in self.etagen:
            statusString+= f"Floor {etage.etagennummer}\n"
            for platz in etage.parkplaetze:
                statusString+= f"{platz} \n"
        statusString+= "----------------------------------"
        return statusString
    


    
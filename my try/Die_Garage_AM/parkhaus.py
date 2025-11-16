from etage import Etage
from parkplatz import Parkplatz
from fahrzeug import Fahrzeug
class Parkhaus:
    """Die Hauptklasse zur Verwaltung des Parkhauses."""
    def __init__(self,anzahl_etagen,parkplases):
        self.etagen = [] 
        self.configEtage(anzahl_etagen, parkplases)
        self.geparkte_fahrzeuge = {} # Speichert nun direkt den Parkplatz

    def configEtage(self, anzahl_etagen, parkplases):
        """Erstellt die Etagen-Objekte."""
        for i in range(1, anzahl_etagen + 1):
            self.etagen.append(Etage(i, parkplases))
        gesamt_plaetze = anzahl_etagen* parkplases
        print(f"Parkhaus mit {anzahl_etagen} Etagen und {gesamt_plaetze} Plätzen initialisiert.")

    def parken(self, fahrzeug: Fahrzeug) -> str:
        """Weist einem einfahrenden Fahrzeug einen freien Platz zu."""
        
        # 1. Eindeutigkeitsprüfung
        if fahrzeug.id in self.geparkte_fahrzeuge:
            return f"Ablehnung: Fahrzeug {fahrzeug.id} ist bereits im Parkhaus."

        # 2. Platzsuche und Zuweisung 
        for etage in self.etagen:
            freier_platz = etage.freiePlatz() 
            if freier_platz:
                freier_platz.getParkplaces(fahrzeug)
                # Speichert nun den Parkplatz direkt
                self.geparkte_fahrzeuge[fahrzeug.id] = freier_platz 
                return (f"Erlaubt: {fahrzeug} parkt auf Etage {etage.etagennummer}, "
                        f"Parkplatz {freier_platz.nummer}.")
        # 3. Ablehnung
        return f"Ablehnung: Keine freien Plätze vorhanden."
    
    def verlassen(self, fahrzeug_id: str) -> str:
        """Lässt ein Fahrzeug das Parkhaus verlassen und gibt den Platz frei."""
        #fahrzeug_id = fahrzeug_id.upper()

        # 1. Fahrzeug-Ortung und Platz-Freigabe
        if fahrzeug_id not in self.geparkte_fahrzeuge:
             return f"Fehler: Fahrzeug mit ID {fahrzeug_id} wurde im Parkhaus nicht gefunden."
        
        # Holt den Parkplatz, den das Fahrzeug belegt hat
        platz = self.geparkte_fahrzeuge[fahrzeug_id]
        
        # Findet die Etage (wird benötigt, um die Etagen-Nummer auszugeben)
        etage = None
        for e in self.etagen:
            if platz in e.parkplaetze:
                etage = e
                break
        platz.freigeben()
        del self.geparkte_fahrzeuge[fahrzeug_id] # Entfernt den Eintrag aus der Verwaltung
        
        return (f"Erfolg: (ID: {fahrzeug_id}) hat das Parkhaus von Etage "
                f"{etage.etagennummer}, Parkplatz {platz.nummer} verlassen.")
    
    def get_position(self, fahrzeug_id: str) -> str:
        """Fragt die Position eines bestimmten Fahrzeugs ab."""
        #fahrzeug_id = fahrzeug_id.upper()
        
        if fahrzeug_id not in self.geparkte_fahrzeuge:
            return f"Info: Fahrzeug mit ID {fahrzeug_id} parkt derzeit nicht im Parkhaus."

        platz = self.geparkte_fahrzeuge[fahrzeug_id]
        
        # Etage finden
        etage = None
        for e in self.etagen:
            if platz in e.parkplaetze:
                etage = e
                break
        #etage = next(e for e in self.etagen if platz in e.parkplaetze)
        
        return (f"Position: Fahrzeug {fahrzeug_id} befindet sich auf **Etage {etage.etagennummer}**, "
                f"**Parkplatz {platz.nummer}**.")


    def get_freie_plaetze_anzahl(self) -> str:
        """Gibt die Gesamtanzahl der noch freien Parkplätze zurück."""
        gesamt_freie = 0
        
        for etage in self.etagen:
            gesamt_freie += etage.get_freier_platz_anzahl()
        
        return f"Freie Plätze gesamt: {gesamt_freie}"
    
class Parkplatz:
    """Repräsentiert einen einzelnen Parkplatz."""
    def __init__(self, nummer):
        self.nummer = nummer
        self.parked_fahrzeug = None

    def getStatus(self):
        """Prüft, ob der Parkplatz belegt ist."""
        return self.parked_fahrzeug is not None # True, wenn ist belegt
    
    def parkCar(self, fahrzeug):
        """Weist dem Parkplatz ein Fahrzeug zu."""
        self.parked_fahrzeug = fahrzeug

    def freigeben(self):
        """Gibt den Parkplatz frei."""
        self.parked_fahrzeug = None

    def __str__(self):
        status = "BELEGT" if self.getStatus() else "FREI"
        info = f" ({self.parked_fahrzeug.id})" if self.getStatus() else ""
        return f"P-{self.nummer} : {status}{info}"
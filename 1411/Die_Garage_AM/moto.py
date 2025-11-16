from fahrzeug import Fahrzeug

class Moto(Fahrzeug):
    """Repräsentiert ein Motorrad."""
    def __init__(self, id):
        super().__init__(id, "Motorrad")


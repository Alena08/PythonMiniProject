from fahrzeug import Fahrzeug

class Car(Fahrzeug):
    """Repräsentiert ein Auto."""
    def __init__(self, id):
        super().__init__(id, "Auto")


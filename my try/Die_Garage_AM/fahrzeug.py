class Fahrzeug:
    def __init__(self, id, typ):
        self.id = id
        #self.status = False # nicht in Garage
        self.typ = typ

    def __str__(self):
        return f"{self.typ}(ID: {self.id})"
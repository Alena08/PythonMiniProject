from .daten import Kunde

class KundenManager:
    def __init__(self):
        self.kunden = []

    def add_kunde(self, kunde:Kunde):
        self.kunden.append(kunde)

class Kunde:
    def __init__(self, kunden_id, name, email):
        self.kunden_id = kunden_id
        self.name = name
        self.email = email

    def zeige_info(self):
        return f"ID: {self.kunden_id} , Name: {self.name}, Email: {self.email}"
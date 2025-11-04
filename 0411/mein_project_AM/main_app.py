from kunden_sys import KundenManager, Kunde
manager = KundenManager()
print("KundenManager erstellt.")
kunde1 = Kunde(101, "Max Mustermann", "max@example.com")
kunde2 = Kunde(102, "Erika Musterfrau", "erika@example.com")
#Hinzufügen Kunden zum Manager
manager.add_kunde(kunde1)
manager.add_kunde(kunde2)

for kunde in manager.kunden:
    print(kunde.zeige_info())
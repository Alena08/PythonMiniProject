from produkt import Produkt
from lager import Lager

pr1 = Produkt("Laptop", "LP001", 1200.50, 10)
pr2 = Produkt("Maus", "M002", 25, 50)
pr3 = Produkt("Bildschirm","BS001",867.99, 25)
pr4 = Produkt("Tastatur","TS005", 87.95, 50)

print("Anzeigedetails für Produkte")
print(pr1.anzeigen_details())
print("."*20)
print(pr2.anzeigen_details())
print("."*20)
print(pr3.anzeigen_details())
print("-"*20)

print("produkte verkaufen")
print(pr2.produkt_verkaufen(60))
print(pr2.anzeigen_details())
print("-"*20)
print(pr1.produkt_verkaufen(5))
print(pr1.anzeigen_details())

print("produkte auffühllen")
pr3.bestand_auffuellen(2)
print("-"*20)
print(pr3.anzeigen_details())
print("*"*20)

lg = Lager()
lg.produkt_hinzufuegen(pr1)
lg.produkt_hinzufuegen(pr2)
lg.produkt_hinzufuegen(pr3)
lg.produkt_hinzufuegen(pr4)

print("."*20)
print("Info für alle Produkten")
for pr in lg.alle_produkte_anzeigen():
    print(pr)
    print("."*20)

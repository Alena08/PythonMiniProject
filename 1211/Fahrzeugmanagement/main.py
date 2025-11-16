from auto import Auto
from fahrzeug import Fahrzeug

autos = [Auto("VW",50,4), Auto("Audi", 30, 2), Fahrzeug("Tesla",40), Fahrzeug("BMW")]

for auto in autos:
    print(auto.beschleunigen())
    print(auto.gesamtbestand_pruefen())


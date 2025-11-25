from dataclasses import dataclass, asdict
import json

@dataclass
class Address:
    city:str
    zipCode:int

@dataclass
class Person:
    name:str
    age:int
    married:bool
    hobby:list
    address:Address

p1 = Person("Alena",30,True,["travell"],Address("Berlin",13156))
p2 = Person("John", 35, False,["ride","football"], Address("London",67345))

personen = [p1,p2]

try:
    with open("person.json", "r") as file:
        daten = json.load(file)
except Exception:
    daten = []

for p in personen:
    daten.append(asdict(p))

with open("person.json","w",encoding="utf-8") as file:
        json.dump(daten,file, indent=2)



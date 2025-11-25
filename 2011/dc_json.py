from dataclasses import dataclass, asdict
import json

@dataclass
class Person:
    name:str
    age:int

p1 =Person("Maya",5)

#JSON-Serialisierung von Data Classes
json_str = json.dumps(asdict(p1),indent=2)
print(p1)
print(json_str)

# Verschachtelte Data Classes automatisch serialisierung
@dataclass
class Address:
    city:str
    zipCode:int

@dataclass
class User:
    name:str
    address: Address

b = User("Max",Address("Koeln",51061))
print(type(asdict(b)))
json_str = json.dumps(asdict(b), indent=2)
print(json_str)


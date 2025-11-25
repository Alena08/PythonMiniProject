# Data Class
from dataclasses import dataclass

@dataclass
class Person:
    name:str
    age:int


p1 = Person("Ali",20)
print(p1.age)

@dataclass
class Car:
    marke : str
    year:int = 2020

ca = Car("Audi")
ca.year = 2024
# ca.modell = "something"
print(ca)

@dataclass(frozen=True)
class Points:
    x: int
    y: int

pt = Points(3,6)
# pt.x = 4 Error
# pt.z = 4 Error
print(pt)
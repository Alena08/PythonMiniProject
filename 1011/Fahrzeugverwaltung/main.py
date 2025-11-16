from fahrzeug import Fahrzeug
auto1 = Fahrzeug("BMW","X5",2025,"weiss")
auto2 = Fahrzeug("VW","golf", 2020, "rot")
auto3 = Fahrzeug("Tesla", "Model Y", 2024, "schwarz")

print(auto1.informationAusgaben())

auto2.starten()
print(auto2.getMotor())
auto2.setFarbe("grün")
print(auto2.informationAusgaben())
print(auto2.fahren())
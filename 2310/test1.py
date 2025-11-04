def berechne_ergebnis(*zahlen, startwert=10, **optionen):
    ergebnis = startwert + sum(zahlen)
    
    if optionen.get("verdoppeln", False):
        ergebnis *= 2
    if optionen.get("abrunden", False):
        ergebnis = int(ergebnis)
    
    return ergebnis


# Lambda-функция
ist_ueber_hundert = lambda ergebnis: ergebnis > 100
print(berechne_ergebnis(1, 2, 3))                               # 16
print(berechne_ergebnis(5, 5, 5, verdoppeln=True))              # 40
print(berechne_ergebnis(0, 10.5, 20.2, abrunden=True))          # 30
print(berechne_ergebnis(50, 20, 15, verdoppeln=True, abrunden=True))  # 170

print(ist_ueber_hundert(170))  # True
print(ist_ueber_hundert(80))   # False

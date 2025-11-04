def berechne_ergebnis(startwert=10, *zahlen, **optionen):    
    #sum = startwert
    #for zahl in zahlen:
    #    sum+=zahl
    sum1 = startwert + sum(zahlen)

    for key,value in optionen.items():
        if key == "verdoppeln" and value == True:
            sum1*=2
        if key == "abrunden" and value == True:
            sum1 = int(sum1)
    return sum1


ist_über_hundert = lambda ergebnis: ergebnis>100

print(berechne_ergebnis(1, 2, 3))
print(berechne_ergebnis(5, 5, 5, verdoppeln=True))
print(berechne_ergebnis(0, 10.5,20.2, abrunden=True))
print(berechne_ergebnis(50, 20, 15,verdoppeln=True,abrunden=True))
print(ist_über_hundert(170))
print(ist_über_hundert(89))
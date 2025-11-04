
def verarbeite_daten(daten, methode=None):
    if methode==None:
        return list(daten)
    else:
        return list(map(methode, daten))

print("Aufruf 1:")
print(verarbeite_daten([1,2,3]))
print("Aufruf 2:")
print(verarbeite_daten([4,5,6],methode=lambda x: x ** 2))
print("Aufruf 3:")
print(verarbeite_daten([10,25,40],methode=lambda x: x/5 - 1))
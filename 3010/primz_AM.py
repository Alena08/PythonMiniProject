# Schreiben Sie Ihren Programmcode hier
# Es wird eine Liste mit Primzahlen benötigt.
# Verwenden Sie Ihre gefundene Lösung aus der vorherigen Aufgabe.

def primz(n):
    # Ermittlung der Primzahlen bis n
    # Rückgabe als Liste
    prim_list =[]
    i = 2
    if n == 1:
        return None
    while n > 1:
       
        while n % i == 0:
            prim_list.append(i)
            n //= i
        if i == 2:
            i += 1
        else:
            i += 2

    return prim_list
###############
### M A I N ###
###############
# print(primz(700))
# print(primz(2394))
# print(primz(562309))

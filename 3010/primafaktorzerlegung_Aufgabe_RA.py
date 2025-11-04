n = int(input("Gib eine Zahl ein: "))
original = n
faktoren = []
faktor = 2

while n > 1:
    if n % faktor == 0:
        faktoren.append(faktor)
        n = n // faktor
    else:
        faktor += 1

print(original, "=", " * ".join(str(f) for f in faktoren))
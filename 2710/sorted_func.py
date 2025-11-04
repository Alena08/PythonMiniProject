# sorted(iterable, key=None, reverse =False)

zahlen_tuple=(5,2,9,3,7)
zahlen_liste=[5,2,9,3,7]

sortiertes_tuple = tuple(sorted(zahlen_tuple))

sortierte_liste= sorted(zahlen_liste)

print(zahlen_tuple)
print(sortiertes_tuple)

print(zahlen_liste)
print(sortierte_liste)

namen=["Ali","Maria","Alena","Tom","Daria","Reyan"]
absteigend = sorted(namen,reverse=True)

print(absteigend)

worte = ["Python", "ist", "toll","programmieren"]

# sortieren nach Länge
nach_laenge = sorted(worte,key=len)
print(nach_laenge)

buchstaben = ["A","c","b","D"]

# Sortiere alphabetisch, ignoriere Groß/Klein
ignoriere_case = sorted(buchstaben,key=str.lower)
print(ignoriere_case)

personen = [("Ali",45),("Rayen",30),("Alena",35)]

nach_alter= sorted(personen,key=lambda p:p[1])
print(nach_alter)
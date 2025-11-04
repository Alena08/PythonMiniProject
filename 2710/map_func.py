
# map(func, iterable,...)

def quadrat(x):
    return x ** 2

zahlen = [1,2,3,4,5]

#ergebnis_map = map(quadrat,zahlen)

ergebnis_liste = list(map(quadrat,zahlen))
# ergebnis_liste1= [quadrat(x) for x in zahlen] # List Comprehension

print(ergebnis_liste)

zahlen1= [10,20,30]
ergebnis = list(map(lambda x: x*2 ,zahlen1))

print(ergebnis)

liste1 = [1,2,3]
liste2 = [10,20,30]

summe = list(map(lambda x,y: x+y, liste1, liste2))
#summe = list(map(lambda x,y,z: x+y+z, liste1, liste2,zahlen1))

print(summe)


# filter(function, iterable)

# gibt ein filter-objekt zurück

# ergebnis = list(filter(func,iterable))

def ist_gerade(zahl):
    return zahl % 2 == 0

zahlen = [1,2,3,4,5,6,7,8]

gerade_zahlen=list(filter(ist_gerade,zahlen))

print(gerade_zahlen)
# gerade_zahlen_liste = list(gerade_zahlen)
# print(gerade_zahlen_liste)

namen=["Ali","Maria","Alena","Tom","Daria","Reyan"]
#Nur Namen filtern, die mit 'A' beginnen

namen_mit_A=list(filter(lambda name: name.endswith('a'), namen))
print(namen_mit_A)
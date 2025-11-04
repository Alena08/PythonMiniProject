
width = 8
i = 1
j= 1
while i < width :
    leer = width - i + 5 
    print(" " * leer, end="")
    print('* ' * i)
    i+=1

zeile = 1
lange = 4
breite = 3
verschiebung = width + 2  

while zeile <= lange:
    print(" " * verschiebung + "* " * breite)
    zeile += 1
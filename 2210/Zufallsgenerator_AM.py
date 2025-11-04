from random import randint

def zufallsgenerator(anzahl_durchlaufe):
    zahler1 = zahler2 = zahler3 = zahler4 = zahler5 = zahler6  = 0

    for i in range(anzahl_durchlaufe):
        ergebnis = randint(1,6)
        match ergebnis:
            case e if e == 1: zahler1 +=1
            case e if e == 2: zahler2 +=1
            case e if e == 3: zahler3 +=1
            case e if e == 4: zahler4 +=1
            case e if e == 5: zahler5 +=1
            case e if e == 6: zahler6 +=1
    zahler_list = [zahler1, zahler2, zahler3, zahler4, zahler5, zahler6]
    durchschnitt = sum(zahler_list)/6
    print("-"*40)
    print(f"Durchläufe :  {anzahl_durchlaufe}")
    print(f"Durchschnitt: {durchschnitt:.2f}")

    for i in range(len(zahler_list)):
        print(f"Zähler{i+1}: {zahler_list[i]}      Diff: {durchschnitt - zahler_list[i]:.2f}       %: {abs((durchschnitt - zahler_list[i])/durchschnitt*100):.2f}")    

zufallsgenerator(100)
zufallsgenerator(1000)
zufallsgenerator(10_000)
zufallsgenerator(100_000)
zufallsgenerator(1_000_000)
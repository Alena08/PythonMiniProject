from random import randint, choice

def frage():
    #die Funktion generiert eine Aufgabe
    a = randint(1,10)
    b = randint(1,10)
    o = choice('+-*')
    aufgabe = f"{a}{o}{b}"
    return aufgabe

def control(q,ant):
    #die Funktion kontrolliert, 
    # ob die Antwort für die Aufgabe richtig ist
    if ant == eval(q):
        print("Ja, das ist richtig!")
    else:
     print(f"Leider falsch. Die korrekte Antwort lautet: {eval(q)}")
     
while True:
        zahl = input("Wie viele Übungsläufe möchten Sie machen?")
        
        if zahl.isnumeric() and int(zahl)<100:
            print(f"Ok, hier ist deine {zahl} Aufgaben")
            zahl = int(zahl)
            for i in range(zahl):
                schulaufgabe = frage()
                print(f"{schulaufgabe} = ?")
                antwort = int(input())
                control(schulaufgabe, antwort)
            break         
        else:
            print("please choose another number")



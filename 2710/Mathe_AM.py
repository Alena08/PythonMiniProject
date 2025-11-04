from random import randint, choice

def frage():
    #die Funktion generiert eine Aufgabe
    a = randint(1,10)
    b = randint(1,10)
    o = choice('+-*><')
    aufgabe = f"{a}{o}{b}"
    return aufgabe

def ist_zahl(value):
    if value.startswith('-'):
        value = value[1:]
    if value.isdigit():
        return True
    elif value.count('.') ==1:
        return True
    else:
        return False

def check_input_menge():
    while True:
        zahl = input("Wie viele Übungsläufe möchten Sie machen? ")
        if ist_zahl(zahl): 
            menge = int(float(zahl))
            if menge < 100:
                return menge
            else:
                print("Ungültige Eingabe! Muss weniger 100 sein.")
        else:
            print("Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")

def check_input_antwort():
    while True:
        ant = input("")
        if ist_zahl(ant):
            schuler_antwort = int(ant)
            return schuler_antwort 
        elif ant in ["Wahr", "w","Falsch", "f"]:
            if ant =="Wahr" or ant=="w":
                ant = True
            elif ant == "Falsch" or ant =="f":
                ant = False
            return ant
        else: 
            print("Ungültige Eingabe!")   

def control(q,ant):
    #die Funktion kontrolliert, 
    # ob die Antwort für die Aufgabe richtig ist

    if ant == eval(q):
        print("Ja, das ist richtig!")
    else:
     print(f"Leider falsch. Die korrekte Antwort lautet: {eval(q)}")
    

zahl = check_input_menge() 
print(f"Ok, hier ist deine {zahl} Aufgaben")
for i in range(zahl):
    schulaufgabe = frage()
    print(f"{schulaufgabe} = ?")
    antwort = check_input_antwort()
    control(schulaufgabe, antwort)


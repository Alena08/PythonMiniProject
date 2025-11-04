from random import randint, choice

def frage():
    #die Funktion generiert eine Aufgabe
    a = randint(1,10)
    b = randint(1,10)
    o = choice('+-*')
    aufgabe = f"{a}{o}{b}"
    return aufgabe

def check_input(value):

    # kontroll buchstabe
    if value.startswith('-'):
        value = value[1:]
    
    if value.isnumeric():
        return int(value)
    elif '.' in value:
        value = float(value)
        return int(value)
    elif value in ["Wahr", "w","Falsch", "f"]:
        return value
 #   elif value.strip() == "":
 #       print("another number")
 #       return None
    else:
        print("another number")
        return None


def control(q,ant):
    #die Funktion kontrolliert, 
    # ob die Antwort für die Aufgabe richtig ist
    if ant =="Wahr" or ant=="w":
        ant =True
    elif ant == "Falsch" or ant =="f":
        ant = False

    if str(ant) == str(eval(q)):
        print("Ja, das ist richtig!")
    else:
     print(f"Leider falsch. Die korrekte Antwort lautet: {eval(q)}")
     
while True:
    zahl = input("Wie viele Übungsläufe möchten Sie machen?")
    zahl = check_input(zahl)  
    if not zahl:
        print("gib richtig!!!")
        continue
    elif zahl<100:
        print(f"Ok, hier ist deine {zahl} Aufgaben")
        zahl = int(zahl)
        for i in range(zahl):
            schulaufgabe = frage()
            print(f"{schulaufgabe} = ?")
            #wir kontrollieren die Antwort
            while True:
                antwort = input()
                antwort = check_input(antwort)
                if antwort or antwort==0:
                    control(schulaufgabe, antwort)
                    break
                else: 
                    print("Du muss die Antwort wiederholen") 
                    continue
                #ende kontrolle antwort
        break   




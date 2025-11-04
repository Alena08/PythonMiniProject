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
    elif '.' in value:
        value1 = float(value)
        return True
    else:
        return False
#         abs_value = value1[1:]
# def check_input_zahl(value1):
#     # kontroll buchstabe
#     if value1.startswith('-'):
#         abs_value = value1[1:]
#     #else: 
#     #    value = value1
#     if abs_value.isdigit() and value1[0]=="-":
#         return -int(abs_value)
#     elif value1.isdigit():
#         return int(value1)
#     elif int(value1) == 0:
#         return int(0)
#     elif '.' in value1:
#         value1 = float(value1)
#         return int(value1)
#     else:
#         return None

def check_input_menge():
    while True:
        zahl = input("Wie viele Übungsläufe möchten Sie machen?")
        if ist_zahl(zahl): # and 0<=check_input_zahl(zahl) < 100:
            menge = int(float(zahl))
            return menge
        else:
            print("Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")

def check_input_antwort():
    while True:
        ant = input("antwort")
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
            print("False")   

def control(q,ant):
    #die Funktion kontrolliert, 
    # ob die Antwort für die Aufgabe richtig ist
    # if ant =="Wahr" or ant=="w":
    #     ant =True
    # elif ant == "Falsch" or ant =="f":
    #     ant = False

    if str(ant) == str(eval(q)):
        print("Ja, das ist richtig!")
    else:
     print(f"Leider falsch. Die korrekte Antwort lautet: {eval(q)}")

# 🔹 Примеры использования:
    

zahl = check_input_menge() 
print(f"Ok, hier ist deine {zahl} Aufgaben")
for i in range(zahl):
    schulaufgabe = frage()
    print(f"{schulaufgabe} = ?")
    antwort = check_input_antwort()
    print(antwort)
    print(type(antwort))
    control(schulaufgabe, antwort)


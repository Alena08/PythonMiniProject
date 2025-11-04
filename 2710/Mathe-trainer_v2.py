from random import randint, choice

def frage():
    #die Funktion generiert eine Aufgabe
    a = randint(1,10)
    b = randint(1,10)
    o = choice('+-*')
    aufgabe = f"{a}{o}{b}"
    return aufgabe
def check_input(value):
    """
    Проверяет введённые данные:
    Разрешены: int, float (преобразуется в int), отрицательные числа, 'f', 'w'
    """
    # kontroll buchstabe
    if isinstance(value, str):
        value = value.strip()
        if value in ["Wahr", "w","Falsch", "f"]:
            return value

    # controll numbers
    try:
       # num = float(value)  # пробуем перевести в число
        return int(value)     # приводим к int (отбрасываем дробную часть)
    except (ValueError, TypeError):
        return None  # если не число и не f/w → возвращаем None

def control(q,ant):
    #die Funktion kontrolliert, 
    # ob die Antwort für die Aufgabe richtig ist
    if ant =="Wahr" or ant=="w":
        ant =True
    elif ant == "Falsch" or ant =="f":
        ant = False
    else:
        ant = int(ant)

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
                #wir kontrollieren die Antwort
                while True:
                    antwort = input()
                    if antwort in ["Wahr", "w","Falsch", "f"]:
                        control(schulaufgabe, antwort)
                        break
                    elif int(antwort):
                        control(schulaufgabe, antwort)
                        break
                    else: 
                        print("Du muss die Antwort wiederholen") 
                #ende kontrolle antwort   
            break         
        else:
            print("please choose another number")



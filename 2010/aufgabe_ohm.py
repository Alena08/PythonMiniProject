print("Welche Größe berechnen?")
while True:
    b = input("Gib die Buchstabe: R oder I oder U: ")
    if b not in ["U", "R", "I","r", "i","u"]:
    #if b!="U" and b!= "I" and b!="R":
        print("Fehlereingabe!!!!")
        continue
    match b:
        case "R" | "r":   
        #if b =="R":
            u = float(input("Gib Spannung U in Volt: "))
            i = float(input("Gib Stromstärke I in Ampere: "))
            R = u/i
            print(f"Wiederstand ist {R}  \u03A9 (Ohm)")
        case "I":
        #elif b == "I":
            U = float(input("Gib Spannung U in Volt: "))
            R = float(input("Gib Wiederstand R in Ohm: "))
            I = U/R
            print(f"Stromstärke ist {I} Ampere")
        case "U":
        #elif b == "U":
            i = float(input("Gib Stromstärke I in Ampere: "))
            r = float(input("Gib Wiederstand R in Ohm: "))
            U = r*i
            print(f"Spannung {U} Volt")
        case _ :
            print("fehler")
    break

Gewicht = float(input("Gewicht in kg: "))
Groesse = float(input("Größe in cm: "))
Geschlecht = input("Geschlecht(m oder w): ")
BMI = Gewicht/((Groesse*0.01)**2)
if Geschlecht == "m":
    if BMI < 20:
        klass = "Untergewicht"
    elif BMI <25:
        klass = "Normalgewicht"
    elif BMI < 30 :
        klass = "Übergewicht"
    elif BMI < 40:
        klass = "Adipositas"
    else:
        klass = "massive Adipositas"
else:
    if BMI < 19:
        klass = "Untergewicht"
    elif BMI <24:
        klass = "Normalgewicht"
    elif BMI < 30 :
        klass = "Übergewicht"
    elif BMI < 40:
        klass = "Adipositas"
    else:
        klass = "massive Adipositas"
print(f"Ihre BMI ist {BMI:.1f}, dass bedeutet {klass}")
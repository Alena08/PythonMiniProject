Gewicht = float(input("Gewicht in kg: "))
Groesse = float(input("Größe in cm: "))
Geschlecht = input("Geschlecht(m oder w): ")
BMI = Gewicht/((Groesse*0.01)**2)
if Geschlecht == "m":
    match BMI:
        case n if n < 20: klass = "Untergewicht"
        case n if n < 25: klass = "Normalgewicht"
        case n if n < 30: klass = "Übergewicht"
        case n if n < 40: klass = "Adipositas"
        case _: klass = "massive Adipositas"
else:
    match BMI:
        case n if n < 19: klass = "Untergewicht"
        case n if n <= 24: klass = "Normalgewicht"
        case n if n < 30: klass = "Übergewicht"
        case n if n < 40: klass = "Adipositas"
        case _: klass = "massive Adipositas"
print(f"Ihre BMI ist {BMI:.1f}, dass bedeutet {klass}")
def primfaktoren(n):
    """Gibt die Primfaktorzerlegung einer Zahl n als Liste zurück."""
    faktoren = []
    teiler = 2

    while n > 1:
        # пока n делится на teiler — делим и добавляем
        while n % teiler == 0:
            faktoren.append(teiler)
            n //= teiler
        teiler += 1
    return faktoren


# 🔹 Eingabe vom Benutzer
zahl = input("Bitte geben Sie eine natürliche Zahl ein: ")

# проверим, что введено целое число > 1
if zahl.isdigit() and int(zahl) > 1:
    n = int(zahl)
    faktoren = primfaktoren(n)

    # красиво выводим результат
    zerlegung = "·".join(str(f) for f in faktoren)
    print(f"{n} = {zerlegung}")
else:
    print("Bitte geben Sie eine natürliche Zahl größer als 1 ein!")

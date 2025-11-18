try:
    with open("Daten1.txt","r+") as file: # 'r+' Lesen und Schreiben
        inhalt = file.read()
        file.write(f"\nZeile 6")

    print(inhalt)
except FileNotFoundError:
    print("Error: File not found")


try:
    with open("datei2.txt","w+") as file:
        inhalt = file.read()
        print(inhalt)
        file.write(f"{inhalt}\nHello again from Python\nHier zweite Zeile")
except Exception as e:
    print(e)

try:
    with open("datei2.txt","a") as file:
        file.write("\nHier 3te Zeile")
except Exception as e:
    print(e)
from parkhaus import Parkhaus
from car import Car
from moto import Moto
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Daten Garage")
root.geometry("500x400")
tk.Label(root, text="Interaktive Konfiguration").grid(column=0, row=0, columnspan=4)
#print("--- 1. Interaktive Konfiguration ---")
    
while True:
    try:
        tk.Label(root, text="Geben Sie die gewünschte Anzahl der Etagen ein ").grid(column=0, row=1, columnspan=2)
        num_etagen = tk.Entry(root).grid(column=0, row=2)
        #num_etagen = int(num_etagen)
        #num_etagen = int(input("Geben Sie die gewünschte Anzahl der Etagen ein (z.B. 4): "))
        if num_etagen < 1:
                print("Die Anzahl der Etagen muss mindestens 1 sein.")
                continue
        break
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")

while True:
    try:
        tk.Label(root, text="Geben Sie die gewünschte Anzahl der Etagen ein ").grid(column=3, row=1, columnspan=2)
        plaetze_pro_etage = tk.Entry(root).grid(column=3, row=2) 
        #plaetze_pro_etage = int(plaetze_pro_etage)
        #plaetze_pro_etage = int(input("Geben Sie die Anzahl der Parkplätze pro Etage ein (z.B. 20): "))
        if plaetze_pro_etage < 1:
            print("Die Anzahl der Plätze muss mindestens 1 sein.")
            continue
        break
    except ValueError:
        print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")

# Parkhaus erstellen
parkhaus_vence = Parkhaus(
    anzahl_etagen=num_etagen, 
    parkplases=plaetze_pro_etage
)

print("\n" + "="*50)


root.mainloop()
# print("\n--- 2. Simulation Start ---")

# # Beispiel-Fahrzeuge
# auto1 = Car("VN-A-100")
# auto2 = Car("VN-A-200")
# bike1 = Moto("VN-M-10")
# #5print(auto2.__dict__)

# # Parken
# print(parkhaus_vence.parken(auto1))
# print(parkhaus_vence.parken(bike1))
# print(parkhaus_vence.parken(auto2))

# print("\n--- 3. Abfragen ---")
# print(parkhaus_vence.get_position("VN-A-200"))
# print(parkhaus_vence.get_freie_plaetze_anzahl())

# print("\n--- 4. Verlassen ---")
# print(parkhaus_vence.verlassen("VN-A-100")) 

# print("\n--- 5. Nach dem Verlassen ---")
# print(parkhaus_vence.get_freie_plaetze_anzahl())

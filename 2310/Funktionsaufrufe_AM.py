def konfiguriere_bestellung(kunden_id, max_anzahl=10, *produkte,**optionen):
    
    print(f"ID: {kunden_id}, Max: {max_anzahl}, Produkte: {produkte},Optionen: {optionen}")

konfiguriere_bestellung(1001,5)
konfiguriere_bestellung(1002,5, "Laptop", "Maus")
#A3
#konfiguriere_bestellung(1003,"Monitor", "Tastatur",max_anzahl=20) # Fehler!
#   Fehler  weil konfiguriere_bestellung() got multiple values for argument 'max_anzahl'
#max_anzahl bekommt doppelt Werte("Monitor" und 20)
#konfiguriere_bestellung(1003, 20, "Monitor", "Tastatur") # Wäre richtig

#A4
#konfiguriere_bestellung(kunden_id=1004, 5, "Stift") #Fehler!
#   Fehler weil 
#   konfiguriere_bestellung(kunden_id=1004, 5, "Stift")
#SyntaxError: positional argument follows keyword argument

#A5
#konfiguriere_bestellung(1005,versandart="Express", 20) Fehker!
#   Fehler weil
#   konfiguriere_bestellung(1005,versandart="Express", 20)
#SyntaxError: positional argument follows keyword argument

#A6
konfiguriere_bestellung(max_anzahl=30, kunden_id=1006,artikel="Buch") 
#   kein Fehler, aber artikel geht zu Optionen, nicht zu Produkten
#   konfiguriere_bestellung(1006, 30, "Buch") Wäre richtig


artikel_liste = ["T-Shirt", "Hose", "Schuhe"]
zusatz_details = {"rabatt": 0.15, "filiale": "Online"}
print(*artikel_liste)
print(*zusatz_details.items())
konfiguriere_bestellung(2001, 8, *artikel_liste, **zusatz_details)
 
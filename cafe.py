milch_liter = 15.75 
kaffee_packungen = 32
zucker_wuerfel = 1023
budget = 250.0
lieferanten_liste = ["Milch-Express","Bohnen-Co","Süß-GmbH"]
#1. Nachschub-Kalkulation
print("Wie viele volle 5-Liter-Kanister: ", milch_liter//5)
print("Wie viel Milch bleibt nach dem Füllen der Kanister übrig? :",milch_liter%5)
print(f"Potenz: {kaffee_packungen**1.05:.2f}")
milch_liter+=4.5
print("Neue Milchbestand",milch_liter)
print("-"*30)
#2. Bestell-Entscheidungen
print("Milch muss nachbestellt werden?:", milch_liter < 15)
print("Ist der Restbestand an Kaffeepackungen genau 32?", kaffee_packungen==32)
print("Muss sowohl Milch als auch Kaffee nachbestellt werden?", kaffee_packungen<10 and milch_liter<15)
print("Eine Bestellung wird ausgelöst?",not (budget <100))
print("-"*30)
#3. Effizienz und Identität
print("Ein neuer Lieferant namens \"Süß-GmbH\" bietet Zucker an. Ist dieser Lieferant bereits in der lieferanten liste?","Süß-GmbH" in lieferanten_liste)
budget_kopie = budget
print("budget und budget_kopie dieselbe?:", budget_kopie is budget)
#4. Zucker-Optimierung (Bitweise Operatoren)
print("Wie viel Kartons für Würfel? (Bitweiser Shift): ",zucker_wuerfel >> 1)
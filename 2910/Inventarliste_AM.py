inventar = [
{"Name": "Axt","Preis": 26.50,"Menge": 5},
{"Name": "Hammer","Preis": 12.99,"Menge": 50},
{"Name": "Säge","Preis": 25.50,"Menge": 5},
{"Name": "Schraubendreher","Preis": 5.00,"Menge": 50},
{"Name": "Bohrer","Preis": 79.99,"Menge": 2},
{"Name": "Zange","Preis": 12.99,"Menge": 50}
]

n = len(inventar)
for i in range(n):
    for j in range(n-i-1):
        if inventar[j]["Menge"] > inventar[j+1]["Menge"]: #Menge vergleich
            temp = inventar[j]
            inventar[j]= inventar[j+1]
            inventar[j+1] = temp
        elif inventar[j]["Menge"] == inventar[j+1]["Menge"]:
            if inventar[j]["Preis"] < inventar[j+1]["Preis"]: #preis vergleich
                inventar[j], inventar[j+1] = inventar[j+1], inventar[j]
            elif inventar[j]["Preis"] == inventar[j+1]["Preis"]:    
                if inventar[j]["Name"] > inventar[j+1]["Name"]: # name vergleich
                    inventar[j], inventar[j+1] = inventar[j+1], inventar[j]

for item in inventar:
    print(f'{item["Name"]} (Menge {item["Menge"]}, Preis {item["Preis"]:.2f})')


#    print(f'{item["Name"]:<{max_name_len}}  (Menge {item["Menge"]:>3}, Preis {item["Preis"]:>7.2f})')
bestellwert = 30
land = None
wohnsitz1 = None #ohne DE
wohnsitz2 = "DE"

b1 = (bestellwert >= 50)
b2 = land 
b3 = wohnsitz1 
b4 = wohnsitz2 

if not b1 and not b2 and not b3 and b4:
    versand = 5 # R1
    print(versand)
elif not b1 and not b2 and b3 and not b4:
    versand = 7.5 # R2
    print(versand)
elif not b1 and b2 and not b3 and not b4:
    versand = 12 # R3
    print(versand)
elif b1 and b2 and not b3 and not b4:
    versand = 10 # R4
    print(versand)
elif b1 and not b2 and b3 and not b4:
    versand = 0  # R5
    print(versand)
elif b1 and not b2 and not b3 and b4:
    versand = 0  # R6
    print(versand)
else:
    print("Keine Regel passt")


#Sortiere eine Liste von Spieler-Scores für eine Bestenliste in einem einfachen Spiel, wobei sowohl der 
#Score als auch der Name berücksichtigt werden sollen (absteigend nach Score, bei Gleichstand alphabetisch nach Name).
# (Spielername, Score)

spieler_scores = [
    ("Eve", 80),
    ("Alice", 150),
    ("Bob", 80),
    ("Charlie", 150),
    ("David", 220),
    
]
print(spieler_scores)
for i in range(len(spieler_scores)):
    for j in range(0, len(spieler_scores)-i-1):
        if spieler_scores[j][1] < spieler_scores[j+1][1]:
            temp = spieler_scores[j] 
            spieler_scores[j] = spieler_scores[j+1]
            spieler_scores[j+1] = temp
        elif spieler_scores[j][1] == spieler_scores[j+1][1]: 
            #kontrolle buchstaben
            if spieler_scores[j][0] > spieler_scores[j+1][0]:
                temp = spieler_scores[j] 
                spieler_scores[j] = spieler_scores[j+1]
                spieler_scores[j+1] = temp
print("sorted liste")
print(spieler_scores)


 
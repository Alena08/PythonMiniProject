# 1: DataFrame Erstellung und erste Inspektion
import pandas as pd

# Erstellt einen Pandas DataFrame mit den folgenden Daten. Nennt ihn buch_verkaeufe.

# | Buchtitel              | Autor         | Genre    | Januar | Februar | März |
# | :--------------------- | :------------ | :------- | :----- | :------ | :--- |
# | Der Ruf des Kuckucks   | Robert Galbraith | Krimi    | 120    | 150     | 130  |
# | Harry Potter und der Stein der Weisen | J.K. Rowling  | Fantasy  | 200    | 180     | 220  |
# | Eine kurze Geschichte der Zeit | Stephen Hawking | Wissenschaft | 80     | 90      | 75   |
# | Stolz und Vorurteil    | Jane Austen   | Klassiker | 95     | 110     | 100  |
# | Die Mitternachtsbibliothek | Matt Haig     | Belletristik | 160    | 170     | 155  |
data = {
    'Buchtitel': [
        'Der Ruf des Kuckucks',
        'Harry Potter und der Stein der Weisen',
        'Eine kurze Geschichte der Zeit',
        'Stolz und Vorurteil',
        'Die Mitternachtsbibliothek'
    ],
    'Autor': [
        'Robert Galbraith',
        'J.K. Rowling',
        'Stephen Hawking',
        'Jane Austen',
        'Matt Haig'
    ],
    'Genre': [
        'Krimi',
        'Fantasy',
        'Wissenschaft',
        'Klassiker',
        'Belletristik'
    ],
    'Januar': [120, 200, 80, 95, 160],
    'Februar': [150, 180, 90, 110, 170],
    'März': [130, 220, 75, 100, 155]
}
df = pd.DataFrame(data)
# Zeigt die ersten 3 Zeilen des DataFrames an.

# Überprüft die Datentypen der Spalten.

# Erhaltet eine Zusammenfassung der statistischen Kennzahlen für die numerischen Spalten.

# 2: Datenzugriff und Filterung

# Wählt nur die Spalten "Buchtitel" und "Autor" aus und zeigt sie an.
# Filtert den DataFrame, um nur Bücher anzuzeigen, die im Januar mehr als 100 Einheiten verkauft haben.
# Findet alle Fantasy-Bücher und zeigt ihre Titel und Verkaufszahlen für März an.

# 3: Neue Spalten und Berechnungen

# Berechnet die "Gesamt_Verkaeufe" für jedes Buch über alle drei Monate (Januar, Februar, März) und fügt diese als neue Spalte dem DataFrame hinzu.
# Findet das Buch mit den höchsten "Gesamt_Verkaeufe".

# 4: Sortieren und Gruppieren
# Sortiert den DataFrame absteigend nach den "Gesamt_Verkaeufe".
# Gruppiert den DataFrame nach "Genre" und berechnet die durchschnittlichen Gesamtverkäufe pro Genre.
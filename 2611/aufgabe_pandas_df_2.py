# Übung: Datenanalyse und -transformation
# Ziel: Bisherige Kenntnisse in Pandas üben, insbesondere im Umgang mit Datenaggregation, Transformation und bedingter Logik.

# Ihr arbeitet weiterhin für das Online-Buchgeschäft. Neben den Verkaufsdaten habt ihr nun auch Informationen zu den Kunden erhalten.

# Aufgabe 1: Laden und Vorbereiten der Daten

# Erstellt zwei Pandas DataFrames:

# buch_verkaeufe: Wie in den vorherigen Übungen (mit den Spalten 'Buchtitel', 'Autor', 'Genre', 'Januar', 'Februar', 'März', 'Gesamt_Verkaeufe').
# kunden: Mit den Spalten 'KundenID', 'Genre_Praeferenz', 'Anmeldedatum'. Hier sind ein paar Beispieldaten:

kunden_data = {
    'KundenID': [1, 2, 3, 4, 5],
    'Genre_Praeferenz': ['Fantasy', 'Krimi', 'Wissenschaft', 'Klassiker', 'Belletristik'],
    'Anmeldedatum': ['2023-01-15', '2023-03-20', '2023-05-10', '2022-11-01', '2023-02-28']
}

#  Konvertiert die Spalte 'Anmeldedatum' im kunden DataFrame in den Datentyp datetime. nutze pd.to_datetime()

# Aufgabe 2: Daten zusammenführen (Merge)

# Führt die beiden DataFrames zusammen, um einen neuen DataFrame verkaeufe_mit_kunden zu erstellen. Verwendet einen geeigneten Merge-Typ, um sicherzustellen, 
# dass alle Verkaufsdaten erhalten bleiben. Die Verknüpfung soll über die Spalte Genre in buch_verkaeufe und Genre_Praeferenz in kunden erfolgen.


# Aufgabe 3: Bedingte Transformation mit np.where()

# Erstellt eine neue Spalte 'Bonus' im verkaeufe_mit_kunden DataFrame.
# Wenn sich ein Kunde vor dem 01.03.2023 angemeldet hat, soll der Bonus 10% der Gesamt_Verkaeufe des entsprechenden Buches betragen.
# Andernfalls soll der Bonus 5% der Gesamt_Verkaeufe betragen.
# Verwendet hierfür die np.where()-Funktion von NumPy.


# Aufgabe 4: Erweiterte Aggregation mit pivot_table()

# Erstellt eine Pivot-Tabelle, um die durchschnittlichen Gesamtverkäufe für jedes Genre zu ermitteln, aufgeteilt nach Anmeldemonat der Kunden.
# Verwendet pivot_table().
# Extrahiert den Anmeldemonat aus der Spalte 'Anmeldedatum' (Tipp: .dt.month).
# Füllt fehlende Werte mit 0.


# Aufgabe 5: String-Operationen mit .str

# Erstellt eine neue Spalte 'Autor_Nachname' im buch_verkaeufe DataFrame, die nur den Nachnamen des Autors enthält. Verwendet .str.split() und Indexierung, um den Nachnamen zu extrahieren.

# Analyse der Trinkgelder in Restaurants
Sie sind Datenanalyst und möchten das Trinkgeldverhalten in einem Restaurant untersuchen. 
Ihnen liegt ein Datensatz mit Informationen zu Rechnungen, Trinkgeldern, Geschlecht des Gastes, 
Rauchstatus, Wochentag, Uhrzeit und Größe der Gruppe vor.

Ziel: Finden Sie heraus, wie sich das durchschnittliche Trinkgeld (in Euro) und der durchschnittliche 
Prozentsatz des Trinkgeldes in Abhängigkeit vom Wochentag und der Uhrzeit des Besuchs unterscheiden.
Datensatz: Verwenden Sie den tips-Datensatz, der in der Seaborn-Bibliothek verfügbar ist.

# Schritte zur Lösung:
    * Laden des Datensatzes: Laden Sie den tips-Datensatz von Seaborn in ein Pandas DataFrame.
    * Berechnen des Trinkgeld-Prozentsatzes: Fügen Sie eine neue Spalte namens 'tip_percentage' hinzu, die das Trinkgeld als Prozentsatz der Gesamtrechnung darstellt. Die Formel ist (tip / total_bill) * 100.
    * Analyse mit pivot_table:
        ** Erstellen Sie eine Pivot-Tabelle, die den Wochentag (day) als Index und die Uhrzeit (time) als Spalten verwendet.
        ** Die Werte (values) sollen das durchschnittliche 'tip' (Trinkgeld) und der durchschnittliche 'tip_percentage' sein.
        ** Verwenden Sie die Funktion np.mean (oder einfach 'mean') als Aggregationsfunktion.
    * Analyse mit groupby:
        ** Führen Sie eine groupby-Operation auf den Spalten ['day', 'time'] durch.
        ** Berechnen Sie den Durchschnitt (mean) für die Spalten 'tip' und 'tip_percentage'.
        ** Vergleichen Sie die Ergebnisse von pivot_table und groupby. Was stellen Sie fest?

Hinweise:
Verwenden Sie import pandas as pd und import seaborn as sns.
Für die Aggregationsfunktion bei pivot_table können Sie aggfunc='mean' oder aggfunc=np.mean verwenden.
Wenn Sie mehrere Aggregationen durchführen möchten, können Sie ein Dictionary 
übergeben, z.B. aggfunc={'tip': 'mean', 'tip_percentage': 'mean'}.


# Aufgabe 1: Dataset laden und Überblick verschaffen

Importiert die Bibliotheken pandas und seaborn. (Tipp: import pandas as pd und import seaborn as sns)
Ladet das titanic-Dataset mit sns.load_dataset('titanic') in eine Variable namens df.
Zeigt die ersten 5 Zeilen des df-DataFrames an, um einen ersten Überblick zu bekommen. (Tipp: Nutzt eine Methode,
                                                                                         die die Kopfzeile zeigt.)


# Aufgabe 2: Eine Kopie erstellen mit .copy()

Manchmal ist es besser, eine Kopie eurer Daten zu erstellen, bevor ihr Änderungen vornehmt. So bleibt das Original 
immer unangetastet.

Erstellt eine Kopie eures df-DataFrames und speichert sie in einer neuen Variable namens df_working.
Zeigt die ersten 5 Zeilen von df_working an, um zu bestätigen, dass die Kopie erfolgreich war.

# Aufgabe 3: Einzigartige Werte finden mit .unique()

Findet heraus, welche verschiedenen Werte in einer bestimmten Spalte vorhanden sind.

Findet alle einzigartigen Werte in der Spalte embarked (das ist der Hafen, von dem die Passagiere eingeschifft sind) 
aus eurem df_working-DataFrame.
Gebt das Ergebnis aus.


# Aufgabe 4: Häufigkeiten zählen mit .value_counts()

Zählt, wie oft jeder einzigartige Wert in einer Spalte vorkommt.

Zählt die Häufigkeit der verschiedenen Werte in der Spalte class (Passagierklasse) aus eurem df_working-DataFrame.
Gebt das Ergebnis aus.



# Aufgabe 5: Daten gruppieren und zusammenfassen mit .groupby() und .agg()

Diese Funktionen sind super mächtig, um Daten nach bestimmten Kriterien zu analysieren und zusammenzufassen.

Gruppiert den df_working-DataFrame nach den Spalten sex (Geschlecht) und pclass (Passagierklasse).
Berechnet für jede Gruppe die folgenden Aggregationen:
Das Durchschnittsalter (age).
Den durchschnittlichen Fahrpreis (fare).
Die Anzahl der Überlebenden (survived).
Tipp: Für die Aggregationen könnt ihr Namen vergeben, z.B. durchschnitts_alter=('age', 'mean').
Wichtig: Nutzt am Ende .reset_index(), um die Gruppierungsschlüssel als normale Spalten im Ergebnis-DataFrame zu erhalten.
Speichert das Ergebnis in einer Variable (z.B. grouped_results) und gebt es aus.

# Aufgabe 6: Altersgruppen erstellen mit .cut()

Wir können numerische Daten in Kategorien (sogenannte "Bins") einteilen, um sie besser zu analysieren.

Wichtig: Die age-Spalte hat fehlende Werte. Bevor ihr cut() nutzen könnt, müsst ihr diese auffüllen. Füllt sie mit dem Durchschnittsalter aller Passagiere auf. (Tipp: Nutzt df_working['age'].fillna(...) und inplace=True.)
Definiert Altersbereiche (Bins) und passende Labels (Namen) für die Altersgruppen:
Bins: [0, 12, 18, 60, 100] (Dies sind die Altersgrenzen: 0 bis unter 12, 12 bis unter 18, 18 bis unter 60, 60 bis unter 100 Jahre.)
Labels: ['Kind', 'Teenager', 'Erwachsener', 'Senior']
Erstellt eine neue Spalte namens age_group in eurem df_working-DataFrame mithilfe von pd.cut(). (Tipp: Denkt an right=False.)
Zeigt die Spalten age und age_group der ersten 10 Zeilen an, um die neue Spalte zu überprüfen.
Bonus-Aufgabe: Nutzt euer Wissen über groupby() und value_counts(), um zu sehen, wie viele Passagiere jeder neuen Altersgruppe überlebt haben (survived = 1) und wie viele nicht (survived = 0). (Tipp: normalize=True und .unstack() können hier nützlich sein.)
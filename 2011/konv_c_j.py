import csv, json

# CSV lesen
with open("my1.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    daten_liste = list(reader)
    #print(daten_liste)

# In JSON schreiben
with open("my1.json","w", encoding="utf-8") as file:
    json.dump(daten_liste, file, indent=4, ensure_ascii=False)

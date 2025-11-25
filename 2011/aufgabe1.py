import json
# Erstelle ein Python Dict, das eine Person beschreibt:
# speichere diese Dict als JSON-Datei namen pr.json
# Lade die JSON-Datei wieder ein.
# Gib den Namen und des Alter der Person aus.

person = {
    "name":"Alena", 
    "age":30,
    "city":"Berlin"
}
with open("pr.json", "w",encoding="utf-8") as jsonfile:
    json.dump(person, jsonfile, indent=2)

with open("pr.json", "r", encoding="utf-8") as file:
    info = json.load(file)
    print(info["name"], info["age"])

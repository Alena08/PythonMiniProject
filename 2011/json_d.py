
import json

# JSON  = JavaScript Object Notation

person_json = '{"name":"Anna","alter":25,"verheitet": false,"hobbys":["Lesen","sport"],"adresse":{"stadt":"Köln","plz":51063}}'
# JSON-String --> python dict
person_dict = json.loads(person_json)
print(person_dict['name'])

# Pytho-Dict --> JSON-String
personD = {
    "name":"Max",
    "age":30,
    "verheiratet":True
}

json_string = json.dumps(personD, indent=2)
print(json_string)

# JSON Datei Schreiben
with open("personen.json","w",encoding="utf-8") as jsonfile:
    json.dump(personD, jsonfile, indent=2)

# JSON Lesen
with open("person.json","r",encoding="utf-8") as jsonfile:
    daten = json.load(jsonfile)
    print(daten["hobbys"])

# Erstelle ein Python Dict, das eine Person beschreibt:
# name
# age
# city
# speichere diese Dict als JSON-Datei namen pr.json
# Lade die JSON-Datei wieder ein.
# Gib den Namen und des Alter der Person aus.
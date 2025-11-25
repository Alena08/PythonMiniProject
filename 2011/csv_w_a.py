import csv

# with open("iris.txt","r",encoding="utf-8") as txtfile:
# with open("iris.json","r",encoding="utf-8") as jsonfile:
with open("iris.csv","r",encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# Schreiben

with open("neu.csv","w",encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=";") # delimiter
    writer.writerow(["Name","Alter"])
    writer.writerow(["Ali","35"])

# Lesen mit DictReader

with open("my1.csv","r",encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader :
        print(row)
        print(row["Name"],row["Age"],row["City"])

# Schreiben mit DictWriter
fieldnames = ["Name","Address"]
with open("new_person.csv","w",newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f,fieldnames,delimiter=',')
    writer.writeheader()
    writer.writerow({'Name':'Paul','Address':'Straße 1 55223 myCity'})

print('*'*30)
# Filtern
with open("my1.csv","r",encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader :
        if int(row['Age'])> 30:
            print(row["Name"],row["Age"],row["City"])

print('*'*30)
# Sortieren
with open("my1.csv","r",encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    sorted_data = sorted(reader,key=lambda x :int(x['Age']))
    for row in sorted_data :
        print(row)
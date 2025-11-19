import csv

daten = [
["Name", "Age", "City"],
["Ali", 40, "Koln"],
["Alena", 30, "Berlin"]
]

with open("my1.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(daten)
    # writer.writerow(["..."])

# with open("my1.csv","r") as file:
#     reader = csv.reader(file)
#     for line in reader:
#         print(line)
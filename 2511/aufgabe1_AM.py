import pandas as pd

df = pd.DataFrame({
                "Produkt":["Apfel","Birne","Milch","Käse", "Tomate","Durke"],\
                "Preis":["1,20", "0,90", "1.50", "2.40", "0,70", "0.60"],\
                "Anzahl":[30, 45, 20, 10, 50, 40],\
                "Kategorie":["Obst", "Obst", "Milchprodukte", "Milchprodukte", "Gemüse", "Gemüse"]\
                })

#2. Spaltennamen umbenennen
df = df.rename(columns={"Preis":"price","Anzahl":"quantity"})

# 3. Preis zu numerisch
print("-"*20)
df['price']= pd.to_numeric(df['price'].str.replace(",","."), downcast="float")
print(df)

# 4.Neue Spalte berechnen
print("-"*20)
df["total"] = round(df['price']*df['quantity'], 2)
print(df)


#5. Filtern mit loc
print("-"*20)

print(df.loc[df["Kategorie"]=="Obst"])

#6. Zugriff mit iloc
print("-"*20)
print(df.iloc[:3,:2])

#7. Höchster Umsatz
print("-"*20)
print(df.loc[df["total"].idxmax()])
print("-"*20)
print(df.sort_values(by="total", ascending=False))

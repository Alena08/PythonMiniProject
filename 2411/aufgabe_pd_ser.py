import pandas as pd

preise = pd.Series(
    [1.20, 2.50, 3.00, 4.75, 2.10],
    index=["Apfel", "Banane", "Kirsche", "Pfirsich", "Birne"]
)

print(preise)
# 1. Greife mit .loc auf den Preis von „Kirsche“ zu.
print("Kirsche preis",preise.loc["Kirsche"])
print("-"* 50)

# 2. Greife mit .iloc auf den dritten Eintrag der Series zu.
print(preise.iloc[2])
print("-"* 50)
# 3. Gib mit .loc die Preise von „Apfel“ und „Pfirsich“ gleichzeitig aus.
print(preise.loc[["Apfel","Pfirsich"]])
print("-"* 50)
# 4. Gib mit .iloc die letzten zwei Werte aus.
print(preise.iloc[-2:])
print("-"* 50)
# 5. Ändere mit .loc den Preis von „Banane“ auf 2.80.
preise.loc["Banane"] = 2.80
print(preise.loc["Banane"])
print("-"* 50)

# 6. Gib mit .loc alle Früchte aus, deren Preis über 2.00 liegt.
print(preise.loc[preise > 2])
# 7. Gib mit .iloc jeden zweiten Eintrag aus (also Index 0, 2, 4).
print(preise.iloc[::2])
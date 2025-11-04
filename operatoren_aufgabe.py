#1. Arithmetische Operatoren
print("1. Arithmetische Operatoren")
print("15*4 =", 15*4)
print("27//5 =", 27//5)
print("27%5 =", 27%5)
print("4**3 =", 4**3)
print("-"*30)
#2. Relationale (Vergleichs-) Operatoren
print("2. Relationale (Vergleichs-) Operatoren")
print("10>=10 ist", 10>=10)
print('"Apfel"!="apfel" ist',"Apfel"!="apfel")
print("5<5 :", 5<5)
print('len("Python")==6 :',len("Python")==6)
print("-"*30)
#3. Zuweisungsoperatoren
print("3. Zuweisungsoperatoren")
x = 12
print("x =", x)
x+=3
print("x+=3 :", x)
x-=5
print("x-=5 :", x)
x*=2
print("x*=2 :", x)
x//=4
print("x//=4 :", x)
print("-"*30)
#4. Logische Operatoren
print("4. Logische Operatoren")
a = True
b = False
print("a =", a)
print("b =", b)
print("a and b :", a and b)
print("a or b :", a or b)
print("not b :", not b)
print("(a and not b) or b",(a and not b) or b)
print("-"*30)
#5. Mitgliedschaftsoperatoren
print("5. Mitgliedschaftsoperatoren")
meine_liste = [10, 20, 30, 40]
text ="Hallo Welt"
print("Ist 20 in meine liste?", 20 in meine_liste)
print("Ist 50 nicht in meine liste?", 50 not in meine_liste)
print('Ist der Substring "Welt" in text?',"Welt" in text)
print("hallo" in text)
print("-"*30)
#6. Identitätsoperatoren
print("6. Identitätsoperatoren")
x = 10
y = 10
z = 20
print(x is y)
print(x is not z)
a = [1, 2]
b = [1, 2]
print(a is b)
print("-"*30)
#7. Bitweise Operatoren
print("7. Bitweise Operatoren")
A = 5
B = 3
print("A =", A)
print("B =", B)
print("A & B (Bitweises UND) :",A & B)
print("A | B (Bitweises ODER) :", A | B)
print("A ^ B (Bitweises XOR) :", A ^ B)
print("A >> 1 (Bitweises Rechts-Shift um 1) :", A >> 1)
print("-"*30)

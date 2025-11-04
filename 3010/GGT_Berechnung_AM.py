from primz_AM import primz
def ggt_durch_pfz(a,b):
    """
    ggt funktion
    """

    # l1_set = list(set(primz(a)))
    # l2_set = list(set(primz(b)))
    # l3 = l1_set + l2_set
    # l3 = set(l3)
    # ggt =1
    # for i in l3:
    #     ggt *= i
    

    while b:
        a,b = b,a%b
    return a
    return ggt

zahl1 = 16
zahl2 = 24
ergebnis_ggt = ggt_durch_pfz(zahl1, zahl2)
print(f"\nPrimfaktorzerlegung von {zahl1}: {primz(zahl1)}")
print(f"Primfaktorzerlegung von {zahl2}: {primz(zahl2)}")
print(f"Der GGT von {zahl1} und {zahl2} ist: {ergebnis_ggt}")

def kgv_durch_pfz(a, b):
    """
    Berechnet das Kleinste Gemeinsame Vielfache (KGV) von a und b
    mithilfe ihrer Primfaktorzerlegungen.
    """
# Berechnet das Kleinste Gemeinsame Vielfache (KGV) von a und b
# mithilfe ihrer Primfaktorzerlegungen.
# '''

    kgv_wert = (a*b)//ggt_durch_pfz(a,b)
    return kgv_wert

ergebnis_kgv = kgv_durch_pfz(zahl1, zahl2)
print("\n--- KGV-Berechnung ---")
print(f"PFZ von {zahl1}: {primz(zahl1)}")
print(f"PFZ von {zahl2}: {primz(zahl2)}")
print(f"Das KGV von {zahl1} und {zahl2} ist: {ergebnis_kgv}")
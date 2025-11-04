def pythagoras_theorem(a:float, b:float) -> float:
    """
    die fehlende Seite eines rechtwinkligen Dreiecks berechnet
    """
    c = (a**2 +b**2)**0.5
    return c
print(type(pythagoras_theorem(a=3, b=4)))

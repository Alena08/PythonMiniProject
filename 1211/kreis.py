class Kreis:
    PI = 3.14159
    def __init__(self,radius):
        self.radius = radius

    @staticmethod
    def ist_positive(wert):
        return wert>0

    @classmethod
    def aus_umfang(cls, umfang):
        r = umfang/(2*cls.PI)
        return cls(r)
    
kreis1 = Kreis(5)
print(kreis1.radius)
print(Kreis.ist_positive(-5))
k2 = Kreis.aus_umfang(25)
print(k2.radius)

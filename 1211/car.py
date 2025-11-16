class Car:
    __carCounter = 0 # class attribute
    # tripSum = 0
    PI=3.14
    def __init__(self, licensePlate, marke, modell, color):
        self.__licensePlate = licensePlate
        self.__marke = marke
        self.__modell = modell
        self.__color = color
        Car.__carCounter+=1
        #self.marke= self.__marke

    @property # Der Getter
    def marke(self):
        return self.__marke
    
    @marke.setter# Der Setter
    def marke(self, neue_marke):
        self.__marke = neue_marke

    def drive(self):
        return f"Car with License Plate Number {self.__licensePlate} on the way"
    
    @classmethod #Dekorator
    def calculateTrips(cls, trip, euroPerKm): # Als erstes Argument die Klasse(cls)
        #cls.tripSum= trip * euroPerKm
        return trip * euroPerKm
    
    @classmethod
    def getCounter(cls):
        return cls.__carCounter
    
    def __str__(self):
        return f"The Car has License Plate number {self.__licensePlate},\n\
        from {self.__marke} and the modell {self.__modell} and has the color {self.__color}"
    


if __name__ == "__main__":
    car1 = Car("K-N11","Audi","A6","Black")
    car2 = Car("K-N11","Audi","A6","Black")
    car3 = Car("K-N11","Audi","A6","Black")
    
    for i in range(10):
        Car(f"K-N1{i}", "Audi","A6","Black")

    print(car1.marke)
    car1.marke = "VW"
    print(car1.marke)
    print(car1.drive())
    print(Car.calculateTrips(30,5))
    print(car2.calculateTrips(30,5))
    # print(car1.carCounter)
    # print(car2.carCounter)
    print(Car.getCounter())

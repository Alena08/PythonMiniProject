class Wagen:
    def __init__(self, licensePlate, wagenType):
        self.__licensePlate = licensePlate
        self.__wagenType = wagenType
    
    def getLicensePlate(self):
        return self.__licensePlate
    
    def setLicensePlate(self,licensePlate):
        self.__licensePlate = licensePlate

    def getWagenType(self):
        return self.__wagenType
    
    def __str__(self):
        return f"Type: {self.__wagenType}, License Plate: {self.__licensePlate}"
    
class ParkingSpace:

    def __init__(self, spaceNumber):
        self.__spaceNumber = spaceNumber
        self.__isOccupied = False
        self.__wagen = None

    def isOccupied(self):
        return self.__isOccupied
    
    def getWagen(self):
        return self.__wagen
    
    def parkWagen(self,wagen):
        self.__wagen = wagen
        self.__isOccupied = True
    
    def removeWagen(self):
        parkedWagen = self.__wagen
        self.__wagen = None
        self.__isOccupied = False
        return parkedWagen
    
    def getSpaceNumber(self):
        return self.__spaceNumber
    
    def __str__(self):
        return f"Space : {self.__spaceNumber}, status: {"Occupied" if self.__isOccupied else "Free"}, Wagen: {self.__wagen} "

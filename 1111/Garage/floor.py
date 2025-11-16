from parking_space import ParkingSpace

class Floor:
    def __init__(self, floorNumber, numberOfSpaces):
        self.__floorNumber = floorNumber
        self.__spaces = []
        for i in range(numberOfSpaces):
            self.__spaces.append(ParkingSpace(i+1))
    
    def getFloorNumber(self):
        return self.__floorNumber
    
    def getSpaces(self):
        return self.__spaces
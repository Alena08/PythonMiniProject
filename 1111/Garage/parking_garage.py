from floor import Floor

class ParkingGarage:

    def __init__(self, totalFloors, spacesPerFloor):
        self.__totalFloors = totalFloors
        self.__spacesPerFloor = spacesPerFloor

        self.__floors = []
        for i in range(totalFloors):
            self.__floors.append(Floor(i,spacesPerFloor))

    def isWagenAlreadyParked(self, licensePlate):
        """
        Search if a car in the parking garage
        return True or False
        """

        return any(
            space.getWagen().getLicensePlate() == licensePlate
            for floor in self.__floors
            for space in floor.getSpaces()
            if space.isOccupied()
        )
    
    def getStatus(self):
        statusString= "------ Parking Garage Status ------\n"
        for floor in self.__floors:
            statusString+= f"Floor {floor.getFloorNumber()}\n"
            for space in floor.getSpaces():
                statusString+= f"{space} \n"
        statusString+= "----------------------------------"
        return statusString

    def printStatus(self):
        '''
        Prozedure to print
        '''
        print("------ Parking Garage Status ------")
        for floor in self.__floors:
            print("Floor", floor.getFloorNumber())
            for space in floor.getSpaces():
                print(space)
        print("----------------------------------")

    def parkWagen(self, wagen):
        """
        This function searches for the next free space
        and parks the wagen in it
        """
        if(self.isWagenAlreadyParked(wagen.getLicensePlate())):
          print(f"Error: Wagen with license plate {wagen.getLicensePlate()} is already parked.")
          return False
        
        for floor in self.__floors:
            for space in floor.getSpaces():
                if not space.isOccupied():
                    space.parkWagen(wagen)
                    print(f"Wagen: {wagen.getLicensePlate()} Parked Successfully.")
                    return True
        print(f"No free space available for wagen: {wagen.getLicensePlate()}")   
        return False          


    def removeWagen(self, licensePlate):
        '''
        Searches for the car if it a vailable in any park space
        will remove it, if not will give a notification that the
        car is not available in parking garage
        '''
        if(not self.isWagenAlreadyParked(licensePlate)):
          print(f"Error: Wagen with license plate {licensePlate} is not parked.")
          return False
        
        for floor in self.__floors:
            for space in floor.getSpaces():
                if space.isOccupied() and space.getWagen().getLicensePlate() == licensePlate:
                    space.removeWagen()
                    print(f"Wagen: {licensePlate} removed Successfully.")
                    return True
        print(f"No wagen with license plate: {licensePlate} available in the garage")   
        return False  
    
    def findWagenById(self, licensePlate):
        """
        Search for a wagen with  license plate number
        """
        for floor in self.__floors:
            for space in floor.getSpaces():
                if space.isOccupied() and space.getWagen().getLicensePlate() == licensePlate:
                    return f"Wagen with license plate:{licensePlate}\nFloor: {floor.getFloorNumber()}, Space: {space.getSpaceNumber()}"
        
        return f"Wagen with license plate:{licensePlate} not found"



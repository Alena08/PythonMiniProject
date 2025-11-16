from wagen import Wagen
from parking_garage import ParkingGarage

parkhaus = ParkingGarage(2,3)
#parkhaus.printStatus()

w1= Wagen("SM-16","Car")
w2= Wagen("K-16","Car")
parkhaus.parkWagen(w1)
parkhaus.parkWagen(w2)
print(parkhaus.getStatus())
parkhaus.removeWagen("SM-16")
parkhaus.printStatus()
parkhaus.parkWagen(w1)
parkhaus.printStatus()
print(parkhaus.findWagenById("SM-16"))
#print(parkhaus.isWagenAlreadyParked("SM-161"))

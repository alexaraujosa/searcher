from vehicles.Vehicle import Vehicle
from RoadConditions import RoadConditions


class Truck(Vehicle):
    """
    A subclass representing a truck.
    (litros por 100km, peso maximo em kilos, distancia maxima, )
    """
    def __init__(self, averageComsumption=35, currentPeopleStock = 100, maxPeopleHelped=100, maxDistance=1200, speed=90):
        super().__init__("Truck", averageComsumption, currentPeopleStock, maxPeopleHelped, maxDistance, speed)
        self.type = "Land"

    def getVehiclePenalty(self, roadCondition):
        match roadCondition:
            case RoadConditions.NORMAL:
                return 1
            case RoadConditions.STORM:
                return 1.3
            case RoadConditions.FLOOD:
                return 1.7
            case RoadConditions.FOG:
                return 1.2
            case _:
                print("Cant get road penalty for trucks, invalid roadCondition!")
                return -1

    def getTravelTime(self, distance):
        return (distance * 60)/self.speed

    def getFuelNeeded(self, distance):
        return (distance*self.averageComsumption)/100

    def __str__(self):
        return (
            f"Vehicle: {self.name}\n"
            f"Average Consumption: {self.averageComsumption} L/100km\n"
            f"Current people stock: {self.currentPeopleStock}\n"
            f"Max People Helped: {self.maxPeopleHelped}\n"
            f"Max Distance: {self.maxDistance} km\n"
            f"Speed: {self.speed} km/h"
        )
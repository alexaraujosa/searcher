from vehicles.Vehicle import Vehicle
from RoadConditions import RoadConditions


class Helicopter(Vehicle):
    """
    A subclass representing a helicopter.
    Ver heli militar
    """
    def __init__(self, averageConsumption=25, currentPeopleStock = 15, maxPeopleHelped=15, maxDistance=400, speed=200):
        super().__init__("Helicopter", averageConsumption, currentPeopleStock, maxPeopleHelped, maxDistance, speed)
        self.type = "Air"
        self.requires_pilot = True

    def getVehiclePenalty(self, roadCondition):
        match roadCondition:
            case RoadConditions.NORMAL:
                return 1
            case RoadConditions.STORM:
                return 1.5
            case RoadConditions.FLOOD:
                return 1
            case RoadConditions.FOG:
                return 1.4
            case _:
                print("Cant get road penalty for helicopter, invalid roadCondition!")
                return -1

    def getTravelTime(self, distance):
        return (distance * 60)/self.speed

    def getFuelNeeded(self, distance):
        return (self.getTravelTime(distance) * self.averageComsumption)/60

    def __str__(self):
        return (
            f"Vehicle: {self.name}\n"
            f"Average Consumption: {self.averageComsumption} L/h\n"
            f"Current people stock: {self.currentPeopleStock}\n"
            f"Max People Helped: {self.maxPeopleHelped}\n"
            f"Max Distance: {self.maxDistance} km\n"
            f"Speed: {self.speed} km/h"
        )
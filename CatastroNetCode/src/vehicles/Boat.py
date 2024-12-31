from src.vehicles.Vehicle import Vehicle
from src.RoadConditions import RoadConditions


class Boat(Vehicle):
    """
    A subclass representing a boat.
    """
    def __init__(self, averageConsumption=15, maxPeopleHelped=50, maxDistance=300, speed=40):
        super().__init__("Boat", averageConsumption, maxPeopleHelped, maxDistance, speed)
        self.type = "Water"

    def getVehiclePenalty(self, roadCondition):
        match roadCondition:
            case RoadConditions.NORMAL:
                return 1
            case RoadConditions.STORM:
                return 1.6
            case RoadConditions.FLOOD:
                return 1
            case RoadConditions.FOG:
                return 1.3
            case _:
                print("Cant get road penalty for boats, invalid roadCondition!")
                return -1

    def getTravelTime(self, distance):
        return (distance * 60)/self.speed

    def getFuelNeeded(self, distance):
        return (self.getTravelTime(distance) * self.averageComsumption)/60

    def __str__(self):
        return (
            f"Vehicle: {self.name}\n"
            f"Average Consumption: {self.averageComsumption} L/h\n"
            f"Max People Helped: {self.maxPeopleHelped}\n"
            f"Max Distance: {self.maxDistance} km\n"
            f"Speed: {self.speed} km/h"
        )
from src.vehicles.Vehicle import Vehicle
from src.RoadConditions import RoadConditions


class Drone(Vehicle):
    """
    A subclass representing a drone.
    """
    def __init__(self, averageConsumption=0.05, maxPeopleHelped=1, maxDistance=20, speed=50):
        super().__init__("Drone", averageConsumption, maxPeopleHelped, maxDistance, speed)
        self.type = "Air"
        self.requires_pilot = False

    def getVehiclePenalty(self, roadCondition):
        match roadCondition:
            case RoadConditions.NORMAL:
                return 1
            case RoadConditions.STORM:
                return 1.7
            #In case water reflects strong winds
            case RoadConditions.FLOOD:
                return 1.1
            case RoadConditions.FOG:
                return 1.5
            case _:
                print("Cant get road penalty for drones, invalid roadCondition!")
                return -1

    def getTravelTime(self, distance):
        return (distance * 60)/self.speed

    def getFuelNeeded(self, distance):
        return distance * self.averageComsumption

    def __str__(self):
        return (
            f"Vehicle: {self.name}\n"
            f"Average Consumption: {self.averageComsumption} kWh/h\n"
            f"Max People Helped: {self.maxPeopleHelped}\n"
            f"Max Distance: {self.maxDistance} km\n"
            f"Speed: {self.speed} km/h"
        )
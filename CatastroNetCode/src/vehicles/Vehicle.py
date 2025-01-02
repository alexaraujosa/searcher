class Vehicle:
    """
    Superclass for all vehicle types, defining common attributes and methods.
    """

    def __init__(self, name, averageComsumption, currentPeopleStock, maxPeopleHelped, maxDistance, speed):
        self.name = name
        self.averageComsumption = averageComsumption
        self.currentPeopleStock = currentPeopleStock
        self.maxPeopleHelped = maxPeopleHelped
        self.maxDistance = maxDistance
        self.speed = speed

    def calculate_fuel_needed(self, distance):
        """Calculate the amount of fuel or energy needed for a given distance."""
        if distance > self.maxDistance:
            raise ValueError(f"{self.name} cannot travel {distance} km; exceeds max range of {self.maxDistance} km.")
        return distance * self.averageComsumption

    def __str__(self):
        return (
            f"Vehicle: {self.name}\n"
            f"Average Consumption: {self.averageComsumption} units/km\n"
            f"Current people stock: {self.currentPeopleStock} kg\n"
            f"Max People Helped: {self.maxPeopleHelped} kg\n"
            f"Max Distance: {self.maxDistance} km\n"
            f"Speed: {self.speed} km/h"
        )
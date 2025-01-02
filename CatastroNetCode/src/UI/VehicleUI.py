from vehicles.Boat import Boat
from vehicles.Drone import Drone
from vehicles.Helicopter import Helicopter
from vehicles.Truck import Truck

class VehicleUI:
    def __init__(self, vehicles):
        self.runningMain = True
        self.runningUpdater = False
        self.vehicles = vehicles

    def displayMenu(self):
        print("\n=== Vehicle Manager ===")
        print("1. View Current Vehicles")
        print("2. Change Vehicle Values")
        print("3. Exit")

    def displayVehicleOptions(self):
        print("\n=== Vehicle Manager (Value Updater) ===")
        print("1. Boat")
        print("2. Truck")
        print("3. Drone")
        print("4. Helicopter")
        print("5. Exit")

    def displayVehicleConfig(self, vehicle):
        print(f"\n=== Vehicle Manager (Value Updater) ===")
        print(f"1. Change average consumption. (Current value: {vehicle.averageComsumption})")
        print(f"2. Change max people helped. (Current value: {vehicle.maxPeopleHelped})")
        print(f"3. Change max distance. (Current value: {vehicle.maxDistance})")
        print(f"4. Change speed. (Current value: {vehicle.speed})")
        print(f"5. Exit.")

    def viewCurrentVehicles(self):
        for vehicle in self.vehicles:
            print("\n")
            print(vehicle)

    def runMain(self):
        while self.runningMain:
            self.displayMenu()
            choice = input("Select an option: ").strip()

            if choice == "1":
                self.viewCurrentVehicles()
            elif choice == "2":
                self.runningUpdater = True
                self.runUpdater()
            elif choice == "3":
                self.runningMain = False
                print("Exiting Graph Manager. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def updateValue(self, vehicle, choice, value):
        if choice == "1":
            vehicle.averageComsumption = value
        elif choice == "2":
            vehicle.maxPeopleHelped = value
        elif choice == "3":
            vehicle.maxDistance = value
        elif choice == "4":
            vehicle.speed = value

    def boatUpdater(self):
        for vehicle in self.vehicles:
            if isinstance(vehicle, Boat):
                self.displayVehicleConfig(vehicle)
                choice = input("Select an option: ").strip()
                if choice == "5":
                    break

                value = input("Choose new value: ").strip()
                self.updateValue(vehicle, choice, value)
        return

    def droneUpdater(self):
        for vehicle in self.vehicles:
            if isinstance(vehicle, Drone):
                self.displayVehicleConfig(vehicle)
                choice = input("Select an option: ").strip()
                if choice == "5":
                    break

                value = input("Choose new value: ").strip()
                self.updateValue(vehicle, choice, value)
        return

    def truckUpdater(self):
        for vehicle in self.vehicles:
            if isinstance(vehicle, Truck):
                self.displayVehicleConfig(vehicle)
                choice = input("Select an option: ").strip()
                if choice == "5":
                    break

                value = input("Choose new value: ").strip()
                self.updateValue(vehicle, choice, value)
        return

    def helicopterUpdater(self):
        for vehicle in self.vehicles:
            if isinstance(vehicle, Helicopter):
                self.displayVehicleConfig(vehicle)
                choice = input("Select an option: ").strip()
                if choice == "5":
                    break

                value = input("Choose new value: ").strip()
                self.updateValue(vehicle, choice, value)
        return

    def runUpdater(self):
        while self.runningUpdater:
            self.displayVehicleOptions()
            choice = input("Select an option: ").strip()

            if choice == "1":
                self.boatUpdater()
            elif choice == "2":
                self.truckUpdater()
            elif choice == "3":
                self.droneUpdater()
            elif choice == "4":
                self.helicopterUpdater()
            elif choice == "5":
                self.runningUpdater = False
                print("Exiting Graph Manager. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

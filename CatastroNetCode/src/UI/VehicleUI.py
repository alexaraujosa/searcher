
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

    def boatUpdater(self):
        print("Not Implemented")
        return

    def droneUpdater(self):
        print("Not Implemented")
        return

    def truckUpdater(self):
        print("Not Implemented")
        return

    def helicopterUpdater(self):
        print("Not Implemented")
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

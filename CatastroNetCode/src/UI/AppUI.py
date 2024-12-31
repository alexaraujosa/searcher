from src.Graph import Graph
from src.UI.AlgorithmsUI import AlgorithmsUI
from src.UI.GraphUI import GraphUI
from src.UI.VehicleUI import VehicleUI
from src.vehicles.Boat import Boat
from src.vehicles.Drone import Drone
from src.vehicles.Helicopter import Helicopter
from src.vehicles.Truck import Truck


class AppUI():
    def __init__(self):
        self.running = True
        self.graph = Graph()
        self.vehicles = []
        self.graph.load()

    def displayMenu(self):
        print("\n=== App Manager ===")
        print("1. Graph Manager")
        print("2. Algorithm Manager")
        print("3. Vehicles Manager")
        print("4. Exit")

    def openGraphManager(self):
        GraphUI(self.graph).run()
        return

    def openAlgorithmManager(self):
        AlgorithmsUI(self.graph, self.vehicles).run()
        return

    def openVehicleManager(self):
        VehicleUI(self.vehicles).runMain()
        return

    def run(self):
        #Creates standard Vehicles
        boat = Boat()
        self.vehicles.append(boat)
        drone = Drone()
        self.vehicles.append(drone)
        truck = Truck()
        self.vehicles.append(truck)
        helicopter = Helicopter()
        self.vehicles.append(helicopter)

        while self.running:
            self.displayMenu()
            choice = input("Select an option: ").strip()

            if choice == "1":
                self.openGraphManager()
            elif choice == "2":
                self.openAlgorithmManager()
            elif choice == "3":
                self.openVehicleManager()
            elif choice == "4":
                print("Exiting Graph Manager. Goodbye!")
                self.running = False
                break
            else:
                print("Invalid option. Please try again.")

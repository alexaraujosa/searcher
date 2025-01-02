import random
from time import sleep

from algorithms.Dfs import depthFirstSearch
from algorithms.Bfs import breadthFirstSearch
from algorithms.UniformCost import uniformCost
from algorithms.Greedy import greedy


class AlgorithmsUI:
    def __init__(self, graph, vehicles):
        self.running = True
        self.graph = graph
        self.vehicles = vehicles

    def displayMenu(self):
        print("\n=== Algorithm Manager ===")
        print("1. Use DFS")
        print("2. Use BFS")
        print("3. Use UniformCost")
        print("4. Use Greddy")
        print("5. Use Astar")
        print("6. Use AntColony")
        print("7. Dinamic Simulation")
        print("8. Exit")

    def chooseStartEndPoints(self):
        city1_name = input("Which city do you want to start from?: ").strip()
        if self.graph.getCity(city1_name) is None:
            print("Invalid city name.")
            return ("", [])
        city2_names = input("Which cities do you want to assist? (Provide as a list, separated by commas): ").strip()

        end_list = [city.strip() for city in city2_names.split(',')]

        for city in end_list:
            if self.graph.getCity(city) is None:
                print("Invalid city name.")
                return ("", [])

        return (city1_name, end_list)

    def dfs(self):
        """
        Function to start DFS traversal, taking input from the user for the cities.
        The user provides the starting city and the target cities to visit.
        """
        (city1_name, end_list) = self.chooseStartEndPoints()

        (path, totalCostByVehicle) = depthFirstSearch(self.graph, self.vehicles, city1_name, end_list, supplier_list=[])

        self.graph.saveRouteAsPNG(path, end_list, supplier_list=[])
        print("\n=== Path Costs ===")
        print(path)
        print(totalCostByVehicle)
        return

    def bfs(self):
        (city1_name, end_list) = self.chooseStartEndPoints()

        (path, totalCostByVehicle) = breadthFirstSearch(self.graph, self.vehicles, city1_name, end_list, supplier_list=[])
        self.graph.saveRouteAsPNG(path, end_list, supplier_list=[])
        print("\n=== Path Costs ===")
        print(path)
        print(totalCostByVehicle)

        return

    def uniformCost(self):
        (city1_name, end_list) = self.chooseStartEndPoints()

        paths = uniformCost(self.graph, self.vehicles, city1_name, end_list, supplier_list=[])


        #TODO Neste path vai ter de vir um dic com cada veiculo e cada veiculo com um caminho, e um custo associado a cada caminho
        #Assim temos a solução para cada um deles
        #print("\n=== Path Costs ===")
        for vehicle in self.vehicles:
            pathToPrint = []
            print(f"=== Vehicle {vehicle.name} ===")

            for destinies in paths[vehicle.name]:
                for destination, (custo, path) in destinies.items():
                    print(f"=== Destination {destination} ===")
                    print(f"Cost: {custo}, Path: {path}")

                    for city in reversed(path):
                        pathToPrint.insert(0, city)

            self.graph.saveRouteAsPNG(pathToPrint, end_list, supplier_list=[])
            #print(totalCostByVehicle)
        return

    def greddy(self):
        (city1_name, end_list) = self.chooseStartEndPoints()
        
        paths = greedy(self.graph, city1_name, end_list, supplier_list=[])
        finalPath = []
        for path in paths.values():
            finalPath = finalPath + path
        self.graph.saveRouteAsPNG(finalPath, end_list, supplier_list=[])
        print("\n=== Path Costs ===")
        print(finalPath)
        # print(totalCostByVehicle)
        return

    def astar(self):
        return

    def antColony(self):
        print("This content is to be added in future DLC's")
        return

    def dynamicSimulation(self):
        algorithm = ""
        while algorithm != "7":
            algorithm = input(
                "\n=== Dynamic Simulation (Algorithm chooser) ===" +
                "\n1. DFS" +
                "\n2. BFS" +
                "\n3. UniformCost" +
                "\n4. Greddy" +
                "\n5. Astar" +
                "\n6. AntColony" +
                "\n7. Exit" +
                "\nSelect an option: " ,
            ).strip()
            match algorithm:
                case "1":
                    self.dynamicDFS()
                case "2":
                    self.dynamicBFS()
                case "3":
                    self.dynamicUniformCost()
                case "4":
                    self.greddy()
                case "5":
                    self.astar()
                case "6":
                    self.antColony()
                case "7":
                    print("Exiting Graph Manager. Goodbye!")
                case _:
                    print("Invalid option. Please try again.")

    def dynamicDFS(self):
        (city1_name, end_list) = self.chooseStartEndPoints()

        full_path = []
        nEvents = 0

        print("\n=== Starting Dynamic Simulation ===")

        (path, totalCostByVehicle) = depthFirstSearch(self.graph, self.vehicles, city1_name, end_list)

        original_path = path.copy()

        if not path:
            print("No valid path found to the remaining destinations.")
            return

        print("\n=== Initial Path Has Been Calculated ===")
        print(f"Path: {path}")

        print("\n=== Starting traversal ===")

        while end_list:
            current_city = path[0]
            if len(path) > 1:
                next_city = path[1]
            full_path.append(current_city)

            if current_city in end_list:
                end_list.remove(current_city)

            if not end_list:
                break
            if len(path) > 1:
                print(f"Moving from {current_city} to {next_city}...")
            else:
                print(f"Arrived to {current_city}!!")
            sleep(0.3)

            path.pop(0)

            if random.random() < 0.1 and nEvents < 3:
                nEvents += 1
                print("Dynamic event triggered.")
                self.graph.randomizeRoadConditions()
                print("Road conditions updated. Recalculating paths...")
                (path, totalCostByVehicle) = depthFirstSearch(self.graph, self.vehicles, path[0], end_list)

        print("\n=== Comparing choices ===")
        print(original_path)
        print(full_path)

    def dynamicBFS(self):
        (city1_name, end_list) = self.chooseStartEndPoints()

        current_city = city1_name
        remaining_destinations = set(end_list)
        full_path = []

    def dynamicUniformCost(self):
        (city1_name, end_list) = self.chooseStartEndPoints()

        current_city = city1_name
        remaining_destinations = set(end_list)
        full_path = []

    def run(self):
        while self.running:
            self.displayMenu()
            choice = input("Select an option: ").strip()

            if choice == "1":
                self.dfs()
            elif choice == "2":
                self.bfs()
            elif choice == "3":
                self.uniformCost()
            elif choice == "4":
                self.greddy()
            elif choice == "5":
                self.astar()
            elif choice == "6":
                self.antColony()
            elif choice == "7":
                self.dynamicSimulation()
            elif choice == "8":
                print("Exiting Graph Manager. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

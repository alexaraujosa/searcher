import random
from time import sleep

from algorithms.Bidirected.Dfs import depthFirstSearch
from algorithms.Bidirected.Bfs import breadthFirstSearch
from algorithms.Bidirected.UniformCost import uniformCost
from algorithms.Bidirected.Greedy import greedy
from algorithms.Bidirected.Astar import aStarSearch

from algorithms.OnePath.DfsSinglePath import depthFirstSearchSinglePath
from algorithms.OnePath.BfsSinglePath import breadthFirstSearchSinglePath

from algorithms.OnePath.GreedySinglePath import greedySinglePath


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

    def chooseStartEndSupplierPoints(self):
        city1_name = input("Which city do you want to start from?: ").strip()
        if self.graph.getCity(city1_name) is None:
            print("Invalid city name.")
            return ("", [], [])

        city2_names = input("Which cities do you want to assist? (Provide as a list, separated by commas): ").strip()

        end_list = [city.strip() for city in city2_names.split(',')]

        for city in end_list:
            if self.graph.getCity(city) is None:
                print("Invalid city name.")
                return ("", [], [])

        supplier_names = input("Which cities do you want to be suppliers? (Provide as a list, separated by commas): ").strip()

        supplier_list = [supplier.strip() for supplier in supplier_names.split(',')]

        for city in supplier_list:
            if supplier_list == "":
                if self.graph.getCity(city) is None:
                    print("Invalid supplier city name.")
                    return ("", [], [])

        return (city1_name, end_list, supplier_list)

    def dfs(self):
        """
        Function to start DFS traversal, taking input from the user for the cities.
        The user provides the starting city and the target cities to visit.
        """
        (city1_name, end_list, supplier_list) = self.chooseStartEndSupplierPoints()
        if not city1_name or not end_list:
            return

        pathsByGoal = depthFirstSearch(self.graph, self.vehicles, city1_name, end_list, supplier_list)

        pathToPrint = []
        for city in end_list:
            for cities in pathsByGoal[city]:
                pathToPrint.append(cities)

        self.graph.saveRouteAsPNG(pathToPrint, end_list, supplier_list)
        print("\n=== Path Costs ===")
        print(pathsByGoal)
        return

    def dfsOnePath(self):
        """
        Function to start DFS traversal, taking input from the user for the cities.
        The user provides the starting city and the target cities to visit.
        """
        (city1_name, end_list, supplier_list) = self.chooseStartEndSupplierPoints()
        if not city1_name or not end_list:
            return

        print("Calculating path...")
        path = depthFirstSearchSinglePath(self.graph, self.vehicles, city1_name, end_list, supplier_list)

        print("Image generation...")
        self.graph.saveRouteAsPNG(path, end_list, supplier_list)
        print("\n=== Path Costs ===")
        print(path)
        return

    def bfs(self):
        (city1_name, end_list, supplier_list) = self.chooseStartEndSupplierPoints()
        if not city1_name or not end_list:
            return

        pathsByGoal = breadthFirstSearch(self.graph, self.vehicles, city1_name, end_list, supplier_list)

        pathToPrint = []
        for city in end_list:
            for cities in pathsByGoal[city]:
                pathToPrint.append(cities)

        self.graph.saveRouteAsPNG(pathToPrint, end_list, supplier_list)
        print("\n=== Path Costs ===")
        print(pathsByGoal)
        return

        return

    def bfsOnePath(self):
        """
        Function to start DFS traversal, taking input from the user for the cities.
        The user provides the starting city and the target cities to visit.
        """
        (city1_name, end_list, supplier_list) = self.chooseStartEndSupplierPoints()
        if not city1_name or not end_list:
            return

        print("Calculating path...")
        path = breadthFirstSearchSinglePath(self.graph, self.vehicles, city1_name, end_list, supplier_list)

        print("Image generation...")
        self.graph.saveRouteAsPNG(path, end_list, supplier_list)
        print("\n=== Path Costs ===")
        print(path)
        return

    def uniformCost(self):
        (city1_name, end_list, supplier_list) = self.chooseStartEndSupplierPoints()
        if not city1_name or not end_list:
            return

        paths = uniformCost(self.graph, self.vehicles, city1_name, end_list, supplier_list)


        #TODO Neste path vai ter de vir um dic com cada veiculo e cada veiculo com um caminho, e um custo associado a cada caminho
        #Assim temos a solução para cada um deles
        #print("\n=== Path Costs ===")
        for vehicle in self.vehicles:
            pathToPrint = []
            print(f"=== Vehicle {vehicle.name} ===")

            # Iterate through the destinations for the vehicle
            for destination, (cost, path) in paths[vehicle.name].items():
                print(f"=== Destination {destination} ===")
                print(f"Cost: {cost}, Path: {path}")

                # Add the path to the print list in reverse order
                for city in reversed(path):
                    pathToPrint.insert(0, city)

            # Save the route for the vehicle
            self.graph.saveRouteAsPNG(pathToPrint, end_list, supplier_list)

        return

    def greddy(self):
        (city1_name, end_list, supplier_list) = self.chooseStartEndSupplierPoints()
        if not city1_name or not end_list:
            return
        backEndList = end_list.copy()
        
        paths = greedy(self.graph, city1_name, end_list, supplier_list)
        pathToPrint = []
        for destination in paths:
            path = paths[destination]
            cost = self.graph.pathCost(path, [destination], self.vehicles, 0)
            print(f"=== Destitation {destination} ===")
            print(f"Cost: {cost}")
            print(f"Path: {path}")
            pathToPrint = pathToPrint + path

        self.graph.saveRouteAsPNG(pathToPrint, backEndList, supplier_list)
        return

    def greedyOnePath(self):
        """
        Function to start DFS traversal, taking input from the user for the cities.
        The user provides the starting city and the target cities to visit.
        """
        (city1_name, end_list, supplier_list) = self.chooseStartEndSupplierPoints()
        if not city1_name or not end_list:
            return

        print("Calculating path...")
        path = greedySinglePath(self.graph, self.vehicles, city1_name, end_list, supplier_list)

        print("Image generation...")
        self.graph.saveRouteAsPNG(path, end_list, supplier_list)
        print("\n=== Path Costs ===")
        print(path)
        return

    # def astar(self):
    #     (city1_name, end_list, supplier_list) = self.chooseStartEndSupplierPoints()
    #     if not city1_name or not end_list:
    #         return

    #     for city in end_list:
    #         if self.graph.getCity(city) is None:
    #             print("Invalid city name.")
    #             return


    #     paths = uniformCost(self.graph, self.vehicles, city1_name, end_list, supplier_list)

    #     #Assim temos a solução para cada um deles
    #     #print("\n=== Path Costs ===")
    #     for vehicle in self.vehicles:
    #         pathToPrint = []
    #         print(f"=== Vehicle {vehicle.name} ===")

    #         # Iterate through the destinations for the vehicle
    #         for destination, (cost, path) in paths[vehicle.name].items():
    #             print(f"=== Destination {destination} ===")
    #             print(f"Cost: {cost}, Path: {path}")

    #             # Add the path to the print list in reverse order
    #             for city in reversed(path):
    #                 pathToPrint.insert(0, city)

    #         # Save the route for the vehicle
    #         self.graph.saveRouteAsPNG(pathToPrint, end_list, supplier_list)

    #     return

    # def greddy(self):
    #     (city1_name, end_list, supplier_list) = self.chooseStartEndSupplierPoints()
        
    #     paths = greedy(self.graph, city1_name, end_list, supplier_list)
    #     finalPath = []
    #     for path in paths.values():
    #         finalPath = finalPath + path
    #     self.graph.saveRouteAsPNG(finalPath, end_list, supplier_list)
    #     print("\n=== Path Costs ===")
    #     print(finalPath)
    #     # print(totalCostByVehicle)
    #     return

    def astar(self):
        (city1_name, end_list, supplier_list) = self.chooseStartEndSupplierPoints()

        paths = aStarSearch(self.graph, self.vehicles, city1_name, end_list, supplier_list)

        for vehicle in self.vehicles:
            pathToPrint = []
            print(f"=== Vehicle {vehicle.name} ===")

            # Iterate through the destinations for the vehicle
            for destination, (cost, path) in paths[vehicle.name].items():
                print(f"=== Destination {destination} ===")
                print(f"Cost: {cost}, Path: {path}")

                # Add the path to the print list in reverse order
                for city in reversed(path):
                    pathToPrint.insert(0, city)

            # Save the route for the vehicle
            self.graph.saveRouteAsPNG(pathToPrint, end_list, supplier_list)


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
                    self.dynamicGreedy()
                case "5":
                    self.dynamicAstar()
                case "6":
                    self.antColony()
                case "7":
                    print("Exiting Graph Manager. Goodbye!")
                case _:
                    print("Invalid option. Please try again.")

    def dynamicDFS(self):
        (city1_name, end_list, supplier_list) = self.chooseStartEndSupplierPoints()
        if not city1_name or not end_list:
            return

        full_path = {city: [] for city in end_list}
        nEvents = 0

        print("\n=== Starting Dynamic Simulation ===")

        pathsByGoal = depthFirstSearch(self.graph, self.vehicles, city1_name, end_list, supplier_list)

        original_paths = {city: path[:] for city, path in pathsByGoal.items()}

        for city in end_list:
            if not pathsByGoal[city]:
                print(f"Didn't find any path for {city}.")

        print("\n=== Initial Paths Have Been Calculated ===")

        for city in end_list:
            print(f"For {city}: {pathsByGoal[city]}")

        print("\n=== Starting traversal ===")

        remaining_goals = end_list[:]

        while remaining_goals :
            print("\n---------- Voyage Information ----------")
            for city in remaining_goals[:]:
                path = pathsByGoal[city]
                if len(path) > 1:
                    print(f"The convoy going to {city}, moved from {path[0]} to {path[1]}.")
                    full_path[city].append(path.pop(0))  # Append current node and move to next
                elif len(path) == 1:
                    print(f"The convoy going to {city} arrived!")
                    full_path[city].append(path.pop(0))  # Append the final node
                    remaining_goals.remove(city)

            sleep(0.5)

            if random.random() < 0.1 and nEvents < 3:
                print("Dynamic event triggered.")
                nEvents += 1
                self.graph.randomizeRoadConditions()
                print("Road conditions updated. Recalculating paths...")
                for city in remaining_goals:
                    current_node = pathsByGoal[city][0] if pathsByGoal[city] else city1_name
                    newRoutes = depthFirstSearch(self.graph, self.vehicles, current_node, [city], supplier_list)
                    pathsByGoal[city] = newRoutes[city]

        print("\n=== Comparing Choices ===")
        print("Old Routes:")
        for city, path in original_paths.items():
            print(f"{city}: {path}")

        print("New Routes:")
        for city, path in full_path.items():
            print(f"{city}: {path}")

    def dynamicBFS(self):
        (city1_name, end_list, supplier_list) = self.chooseStartEndSupplierPoints()
        if not city1_name or not end_list:
            return

        full_path = {city: [] for city in end_list}
        nEvents = 0

        print("\n=== Starting Dynamic Simulation ===")

        pathsByGoal = breadthFirstSearch(self.graph, self.vehicles, city1_name, end_list, supplier_list)

        original_paths = {city: path[:] for city, path in pathsByGoal.items()}

        for city in end_list:
            if not pathsByGoal[city]:
                print(f"Didn't find any path for {city}.")

        print("\n=== Initial Paths Have Been Calculated ===")

        for city in end_list:
            print(f"For {city}: {pathsByGoal[city]}")

        print("\n=== Starting traversal ===")

        remaining_goals = end_list[:]

        while remaining_goals :
            print("\n---------- Voyage Information ----------")
            for city in remaining_goals[:]:
                path = pathsByGoal[city]
                if len(path) > 1:
                    print(f"The convoy going to {city}, moved from {path[0]} to {path[1]}.")
                    full_path[city].append(path.pop(0))  # Append current node and move to next
                elif len(path) == 1:
                    print(f"The convoy going to {city} arrived!")
                    full_path[city].append(path.pop(0))  # Append the final node
                    remaining_goals.remove(city)

            sleep(0.5)

            if random.random() < 0.1 and nEvents < 3:
                print("Dynamic event triggered.")
                nEvents += 1
                self.graph.randomizeRoadConditions()
                print("Road conditions updated. Recalculating paths...")
                for city in remaining_goals:
                    current_node = pathsByGoal[city][0] if pathsByGoal[city] else city1_name
                    newRoutes = breadthFirstSearch(self.graph, self.vehicles, current_node, [city], supplier_list)
                    pathsByGoal[city] = newRoutes[city]

        print("\n=== Comparing Choices ===")
        print("Old Routes:")
        for city, path in original_paths.items():
            print(f"{city}: {path}")

        print("New Routes:")
        for city, path in full_path.items():
            print(f"{city}: {path}")

    def dynamicUniformCost(self):
        city1_name, end_list, supplier_list = self.chooseStartEndSupplierPoints()
        if not city1_name or not end_list:
            return

        full_path = {}
        nEvents = 0

        print("\n=== Starting Dynamic Simulation ===")

        # Call uniformCost, which now returns a nested dictionary
        allPaths = uniformCost(self.graph, self.vehicles, city1_name, end_list, supplier_list)

        # Extract paths by goal from the vehicle dictionaries
        pathsByGoal = {}
        for vehicle, goals in allPaths.items():
            for goal, (cost, path) in goals.items():
                pathsByGoal[goal] = path

        # Create a copy for comparison later
        original_paths = {goal: path[:] for goal, path in pathsByGoal.items()}

        for city in end_list:
            if city not in pathsByGoal or not pathsByGoal[city]:
                print(f"Didn't find any path for {city}.")

        print("\n=== Initial Paths Have Been Calculated ===")
        for city in end_list:
            print(f"For {city}: {pathsByGoal.get(city, [])}")

        print("\n=== Starting Traversal ===")

        remaining_goals = end_list[:]

        while remaining_goals:
            print("\n---------- Voyage Information ----------")
            for city in remaining_goals[:]:  # Iterate over a copy
                path = pathsByGoal.get(city, [])
                if city not in full_path:
                    full_path[city] = []

                if len(path) > 1:
                    print(f"The convoy going to {city}, moved from {path[0]} to {path[1]}.")
                    full_path[city].append(path.pop(0))  # Append current node and move to next
                elif len(path) == 1:
                    print(f"The convoy going to {city} arrived!")
                    full_path[city].append(path.pop(0))  # Append the final node
                    remaining_goals.remove(city)

            sleep(0.5)

            if random.random() < 0.1 and nEvents < 3:
                print("Dynamic event triggered.")
                nEvents += 1
                self.graph.randomizeRoadConditions()
                print("Road conditions updated. Recalculating paths...")

                for city in remaining_goals:
                    current_node = pathsByGoal[city][0] if city in pathsByGoal and pathsByGoal[city] else city1_name
                    updatedPaths = uniformCost(self.graph, self.vehicles, current_node, [city], supplier_list)

                    # Update only the relevant city's path from the returned vehicle dictionary
                    for vehicle, goals in updatedPaths.items():
                        if city in goals:
                            pathsByGoal[city] = goals[city][1]  # Update with the new path

        print("\n=== Comparing Choices ===")
        print("Old Routes:")
        for city, path in original_paths.items():
            print(f"{city}: {path}")

        print("New Routes:")
        for city, path in full_path.items():
            print(f"{city}: {path}")

    def dynamicGreedy(self):
        (city1_name, end_list, supplier_list) = self.chooseStartEndSupplierPoints()
        if not city1_name or not end_list:
            return

        full_path = {city: [] for city in end_list}
        nEvents = 0

        print("\n=== Starting Dynamic Simulation ===")

        pathsByGoal = greedy(self.graph, self.vehicles, city1_name, end_list, supplier_list)

        original_paths = {city: path[:] for city, path in pathsByGoal.items()}

        for city in end_list:
            if not pathsByGoal[city]:
                print(f"Didn't find any path for {city}.")

        print("\n=== Initial Paths Have Been Calculated ===")

        for city in end_list:
            print(f"For {city}: {pathsByGoal[city]}")

        print("\n=== Starting traversal ===")

        remaining_goals = end_list[:]

        while remaining_goals :
            print("\n---------- Voyage Information ----------")
            for city in remaining_goals[:]:
                path = pathsByGoal[city]
                if len(path) > 1:
                    print(f"The convoy going to {city}, moved from {path[0]} to {path[1]}.")
                    full_path[city].append(path.pop(0))  # Append current node and move to next
                elif len(path) == 1:
                    print(f"The convoy going to {city} arrived!")
                    full_path[city].append(path.pop(0))  # Append the final node
                    remaining_goals.remove(city)

            sleep(0.5)

            if random.random() < 0.1 and nEvents < 3:
                print("Dynamic event triggered.")
                nEvents += 1
                self.graph.randomizeRoadConditions()
                print("Road conditions updated. Recalculating paths...")
                for city in remaining_goals:
                    current_node = pathsByGoal[city][0] if pathsByGoal[city] else city1_name
                    newRoutes = greedy(self.graph, self.vehicles, current_node, [city], supplier_list)
                    pathsByGoal[city] = newRoutes[city]

        print("\n=== Comparing Choices ===")
        print("Old Routes:")
        for city, path in original_paths.items():
            print(f"{city}: {path}")

        print("New Routes:")
        for city, path in full_path.items():
            print(f"{city}: {path}")

    def dynamicAstar(self):
        city1_name, end_list, supplier_list = self.chooseStartEndSupplierPoints()
        if not city1_name or not end_list:
            return

        full_path = {}
        nEvents = 0

        print("\n=== Starting Dynamic Simulation ===")

        # Call uniformCost, which now returns a nested dictionary
        allPaths = aStarSearch(self.graph, self.vehicles, city1_name, end_list, supplier_list)

        # Extract paths by goal from the vehicle dictionaries
        pathsByGoal = {}
        for vehicle, goals in allPaths.items():
            for goal, (cost, path) in goals.items():
                pathsByGoal[goal] = path

        # Create a copy for comparison later
        original_paths = {goal: path[:] for goal, path in pathsByGoal.items()}

        for city in end_list:
            if city not in pathsByGoal or not pathsByGoal[city]:
                print(f"Didn't find any path for {city}.")

        print("\n=== Initial Paths Have Been Calculated ===")
        for city in end_list:
            print(f"For {city}: {pathsByGoal.get(city, [])}")

        print("\n=== Starting Traversal ===")

        remaining_goals = end_list[:]

        while remaining_goals:
            print("\n---------- Voyage Information ----------")
            for city in remaining_goals[:]:  # Iterate over a copy
                path = pathsByGoal.get(city, [])
                if city not in full_path:
                    full_path[city] = []

                if len(path) > 1:
                    print(f"The convoy going to {city}, moved from {path[0]} to {path[1]}.")
                    full_path[city].append(path.pop(0))  # Append current node and move to next
                elif len(path) == 1:
                    print(f"The convoy going to {city} arrived!")
                    full_path[city].append(path.pop(0))  # Append the final node
                    remaining_goals.remove(city)

            sleep(0.5)

            if random.random() < 0.1 and nEvents < 3:
                print("Dynamic event triggered.")
                nEvents += 1
                self.graph.randomizeRoadConditions()
                print("Road conditions updated. Recalculating paths...")

                for city in remaining_goals:
                    current_node = pathsByGoal[city][0] if city in pathsByGoal and pathsByGoal[city] else city1_name
                    updatedPaths = aStarSearch(self.graph, self.vehicles, current_node, [city], supplier_list)

                    # Update only the relevant city's path from the returned vehicle dictionary
                    for vehicle, goals in updatedPaths.items():
                        if city in goals:
                            pathsByGoal[city] = goals[city][1]  # Update with the new path

        print("\n=== Comparing Choices ===")
        print("Old Routes:")
        for city, path in original_paths.items():
            print(f"{city}: {path}")

        print("New Routes:")
        for city, path in full_path.items():
            print(f"{city}: {path}")


    def run(self):
        while self.running:
            self.displayMenu()
            choice = input("Select an option: ").strip()

            if choice == "1":
                print("1. Run DFS in single path.")
                print("2. Run DFS bidirectional.")
                choice2 = input("Select an option: ").strip()
                if choice2 == "1":
                    self.dfsOnePath()
                elif choice2 == "2":
                    self.dfs()
                else:
                    print("Invalid option. Try again.")
            elif choice == "2":
                print("1. Run BFS in single path.")
                print("2. Run BFS bidirectional.")
                choice2 = input("Select an option: ").strip()
                if choice2 == "1":
                    self.bfsOnePath()
                elif choice2 == "2":
                    self.bfs()
                else:
                    print("Invalid option. Try again.")
            elif choice == "3":
                self.uniformCost()
            elif choice == "4":
                self.greddy()
                # self.greedyOnePath()
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

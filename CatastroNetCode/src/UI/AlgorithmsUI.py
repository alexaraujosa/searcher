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
        print("7. Exit")

    def dfs(self):
        """
        Function to start DFS traversal, taking input from the user for the cities.
        The user provides the starting city and the target cities to visit.
        """
        city1_name = input("Which city do you want to start from?: ").strip()
        if self.graph.getCity(city1_name) is None:
            print("Invalid city name.")
            return
        city2_names = input("Which cities do you want to assist? (Provide as a list, separated by commas): ").strip()
        suppliers = input("Which cities do you want to be a supplying station? (Provide as a list, separated by commas): ").strip()

        end_list = [city.strip() for city in city2_names.split(',')]
        supplier_list = [supplier.strip() for supplier in suppliers.split(',')]
    
        for city in end_list:
            if self.graph.getCity(city) is None:
                print("Invalid city name.")
                return

        (path, totalCostByVehicle) = depthFirstSearch(self.graph, self.vehicles, city1_name, end_list, supplier_list)

        self.graph.saveRouteAsPNG(path, end_list, supplier_list)
        print("\n=== Path Costs ===")
        print(path)
        print(totalCostByVehicle)
        return

    def bfs(self):
        city1_name = input("Which city do you want to start from?: ").strip()
        if self.graph.getCity(city1_name) is None:
            print("Invalid city name.")
            return
        city2_names = input("Which cities do you want to assist? (Provide as a list, separated by commas): ").strip()

        end_list = [city.strip() for city in city2_names.split(',')]

        for city in end_list:
            if self.graph.getCity(city) is None:
                print("Invalid city name.")
                return

        (path, totalCostByVehicle) = breadthFirstSearch(self.graph, self.vehicles, city1_name, end_list)
        self.graph.saveRouteAsPNG(path, end_list, supplier_list=[])
        print("\n=== Path Costs ===")
        print(path)
        print(totalCostByVehicle)

        return

    def uniformCost(self):
        city1_name = input("Which city do you want to start from?: ").strip()
        if self.graph.getCity(city1_name) is None:
            print("Invalid city name.")
            return
        city2_names = input("Which cities do you want to assist? (Provide as a list, separated by commas): ").strip()

        end_list = [city.strip() for city in city2_names.split(',')]

        for city in end_list:
            if self.graph.getCity(city) is None:
                print("Invalid city name.")
                return


        paths = uniformCost(self.graph, self.vehicles, city1_name, end_list)

        #TODO Neste path vai ter de vir um dic com cada veiculo e cada veiculo com um caminho, e um custo associado a cada caminho
        #Assim temos a solução para cada um deles
        #self.graph.saveRouteAsPNG(path, end_list)
        #print("\n=== Path Costs ===")
        #print(path)
        #print(totalCostByVehicle)
        return

    def greddy(self):
        city1_name = input("Which city do you want to start from? ").strip()
        if self.graph.getCity(city1_name) is None:
            print("Invalid city name.")
            return
        city2_names = input("Which cities do you want to assist? (Provide as a list, separated by commas): ").strip()

        end_list = [city.strip() for city in city2_names.split(',')]
        for city in end_list:
            if self.graph.getCity(city) is None:
                print("Invalid city name.")
                return
        
        paths = greedy(self.graph, city1_name, end_list)
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
        return

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
                print("Exiting Graph Manager. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

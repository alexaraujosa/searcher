from src.algorithms.Dfs import procuraDFS

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
        procuraDFS(self.graph, self.vehicles, 'Barcelos', 'Ponte de Lima')
        return

    def bfs(self):
        return

    def uniformCost(self):
        return

    def greddy(self):
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

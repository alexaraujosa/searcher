from src.Graph import Graph

class GraphUI:
    def __init__(self, graph):
        self.running = True
        self.graph = graph

    def displayMenu(self):
        print("\n=== Graph Manager ===")
        print("1. Print Graph")
        print("2. Export Current Graph as png")
        print("3. Load Graph From .csv File")
        print("4. Randomize Road Conditions")
        print("5. Exit")

    def displayGraph(self):
        self.graph.printGraph()
        return

    def exportGraph(self):
        self.graph.saveCurrentGraphAsPNG()
        return

    def loadGraph(self, filename):
        if filename == 'default':
            self.graph.load()
        else:
            self.graph.load(filename)
        return

    def randomizeRoadConditions(self):
        self.graph.randomizeRoadConditions()

    def run(self):
        while self.running:
            self.displayMenu()
            choice = input("Select an option: ").strip()

            if choice == "1":
                self.displayGraph()
            elif choice == "2":
                self.exportGraph()
            elif choice == "3":
                graphFile = input("Write a path:<data/graph_data.cvs> or <default>: ").strip()
                self.loadGraph(graphFile)
            elif choice == "4":
                self.randomizeRoadConditions()
            elif choice == "5":
                print("Exiting Graph Manager. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

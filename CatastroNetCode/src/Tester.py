import time
from datetime import datetime

from src.Graph import Graph
from src.algorithms.Bidirected.Bfs import breadthFirstSearch
from src.algorithms.Bidirected.Dfs import depthFirstSearch
from src.algorithms.Bidirected.UniformCost import uniformCost
from src.algorithms.Bidirected.Greedy import greedy
from src.algorithms.Bidirected.Astar import aStarSearch
from src.vehicles.Boat import Boat
from src.vehicles.Drone import Drone
from src.vehicles.Helicopter import Helicopter
from src.vehicles.Truck import Truck

def testAlgorithms(graph, vehicles, start, end_list):
    """
    Run all algorithms on the given graph, vehicles, and start/end cities.
    Log the results into a Results.txt file.
    """

    # Placeholder supplier list
    supplier_list = []

    # Open Results.txt file in append mode
    with open("Results.txt", "w") as file:

        # Timestamp for when the test is being executed
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Test executed at: {timestamp}\n")
        file.write(f"Start City: {start}\n")
        file.write(f"End Cities: {', '.join(end_list)}\n")
        file.write("=" * 50 + "\n")

        def run_algorithm(name, function):
            file.write(f"Running {name}...\n")
            start_time = time.time()

            try:
                result = function(graph, vehicles, start, end_list, supplier_list)
                print(f"{name} result: {result}")  # Debug print
                end_time = time.time()
                elapsed_time = end_time - start_time

                file.write(f"{name} Time: {elapsed_time:.4f} seconds\n")

                if isinstance(result, dict):
                    # Handle BFS, DFS, and Greedy format
                    first_value = next(iter(result.values()))
                    if isinstance(first_value, list):  # {goalCityName: [path]}
                        for goal, path in result.items():
                            file.write(f"{name} Goal: {goal}, Path: {path}\n")
                    elif isinstance(first_value, dict):  # {vehicle: {goalCityName: (cost, [path])}}
                        for vehicle, destinations in result.items():
                            file.write(f"{name} Vehicle: {vehicle}\n")
                            for goal, (cost, path) in destinations.items():
                                file.write(f"  Destination: {goal}, Cost: {cost}, Path: {path}\n")
                elif isinstance(result, tuple):
                    file.write(f"{name} Path: {result[0]}\n")
                    file.write(f"{name} Additional Data: {result[1]}\n")
                else:
                    file.write(f"{name} Result: {result}\n")

            except Exception as e:
                file.write(f"{name} Error: {e}\n")

            file.write("=" * 50 + "\n")

        # Run all algorithms
        run_algorithm("DFS", lambda g, v, s, e, sl: depthFirstSearch(g, v, s, e, sl))
        run_algorithm("BFS", lambda g, v, s, e, sl: breadthFirstSearch(g, v, s, e, sl))
        run_algorithm("Uniform Cost", lambda g, v, s, e, sl: uniformCost(g, v, s, e, sl))
        run_algorithm("Greedy", lambda g, v, s, e, sl: greedy(g, s, e.copy(), sl.copy()))
        run_algorithm("A* Search", lambda g, v, s, e, sl: aStarSearch(g, v, s, e, sl))

        file.write("\n")  # Separate each test with a blank line

# Example usage
if __name__ == "__main__":
    graph = Graph()
    graph.load()
    vehicles = [Boat(), Drone(), Truck(), Helicopter()]

    start = "Vila Nova de Cerveira"  # Replace with your start city
    end_list = ["Albufeira", "Faro"]  # Replace with your end cities

    testAlgorithms(graph, vehicles, start, end_list)

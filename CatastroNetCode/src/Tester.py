import time
from datetime import datetime

from src.Graph import Graph
from src.algorithms.Bfs import breadthFirstSearch
from src.algorithms.Dfs import depthFirstSearch
from src.vehicles.Boat import Boat
from src.vehicles.Drone import Drone
from src.vehicles.Helicopter import Helicopter
from src.vehicles.Truck import Truck


def testAlgorithms(graph, vehicles, start, end_list, dfs_function, bfs_function):
    """
    Run DFS and BFS algorithms on the given graph, vehicles, and start/end cities.
    Log the results into a Results.txt file.

    :param graph: The graph object representing the cities and roads.
    :param vehicles: List of available vehicles for travel.
    :param start: Starting city for the journey.
    :param end_list: List of destination cities to visit.
    :param dfs_function: The depth-first search (DFS) function.
    :param bfs_function: The breadth-first search (BFS) function.
    """

    # Open Results.txt file in append mode
    with open("Results.txt", "a") as file:

        # Timestamp for when the test is being executed
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Test executed at: {timestamp}\n")
        file.write(f"Start City: {start}\n")
        file.write(f"End Cities: {', '.join(end_list)}\n")
        file.write("=" * 50 + "\n")

        # 1. Test DFS
        file.write("Running DFS...\n")
        start_time = time.time()

        dfs_path, dfs_cost_by_vehicle = dfs_function(graph, vehicles, start, end_list)

        end_time = time.time()
        dfs_time = end_time - start_time

        # Log DFS results
        file.write(f"DFS Time: {dfs_time:.4f} seconds\n")
        if dfs_path:
            file.write(f"DFS Path: {', '.join([str(p) for p in dfs_path])}\n")
        else:
            file.write("DFS Path: No solution found.\n")

        if dfs_cost_by_vehicle:
            file.write(f"DFS Costs by Vehicle: {dfs_cost_by_vehicle}\n")
        else:
            file.write("DFS Costs: No cost calculated.\n")

        file.write("=" * 50 + "\n")

        # 2. Test BFS
        file.write("Running BFS...\n")
        start_time = time.time()

        bfs_path, bfs_cost_by_vehicle = bfs_function(graph, vehicles, start, end_list)

        end_time = time.time()
        bfs_time = end_time - start_time

        # Log BFS results
        file.write(f"BFS Time: {bfs_time:.4f} seconds\n")
        if bfs_path:
            file.write(f"BFS Path: {', '.join([str(p) for p in bfs_path])}\n")
        else:
            file.write("BFS Path: No solution found.\n")

        if bfs_cost_by_vehicle:
            file.write(f"BFS Costs by Vehicle: {bfs_cost_by_vehicle}\n")
        else:
            file.write("BFS Costs: No cost calculated.\n")

        file.write("=" * 50 + "\n")
        file.write("\n")  # Separate each test with a blank line


# Example usage:
# You should replace `dfs_function` and `bfs_function` with the actual implementations.
# If you're calling the function within the same file, replace them with `depthFirstSearch` and `breadthFirstSearch`.

if __name__ == "__main__":
    # Replace with your actual graph, vehicles, start city, and end cities
    graph = Graph()# Placeholder - replace with your graph object
    graph.load()
    vehicles = []  # Placeholder - replace with your list of vehicles
    start = "Vila Nova de Cerveira"  # Placeholder - replace with your start city
    end_list = ["Albufeira", "Faro"]  # Placeholder - replace with your list of end cities

    # Add your vehicles
    boat = Boat()
    vehicles.append(boat)
    drone = Drone()
    vehicles.append(drone)
    truck = Truck()
    vehicles.append(truck)
    helicopter = Helicopter()
    vehicles.append(helicopter)


    # Call actual DFS and BFS functions
    def dfs_function(graph, vehicles, start, end_list):
        # Replace with your actual DFS function
        return depthFirstSearch(graph, vehicles, start, end_list, [])


    def bfs_function(graph, vehicles, start, end_list):
        # Replace with your actual BFS function
        return breadthFirstSearch(graph, vehicles, start, end_list)


    # Run the tester
    testAlgorithms(graph, vehicles, start, end_list, dfs_function, bfs_function)

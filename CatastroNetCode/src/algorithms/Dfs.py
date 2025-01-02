from time import sleep

from Graph import Graph
from RoadConditions import RoadConditions
from vehicles.Vehicle import Vehicle

def depthFirstSearch(graph, vehicles, start, end_list, supplier_list, path=None, visited=None, remaining=None):
    """
    Depth-First Search (DFS) algorithm to visit all cities in `end_list` starting from `start`.

    :param graph: The graph containing cities and roads.
    :param vehicles: List of vehicles available for travel.
    :param start: Starting city.
    :param end_list: List of cities to visit.
    :param path: Current path being explored (initially None, defaults to empty).
    :param visited: Set of visited cities (initially None, defaults to empty).
    :param remaining: Cities yet to be visited (initially None, defaults to `end_list`).
    :return: The path and total cost of visiting the cities in `end_list` or None if no valid path exists.
    """
    if path is None:
        path = []  # Initialize the path if not provided.
    if visited is None:
        visited = set()  # Set to track visited cities.
    if remaining is None:
        remaining = set(end_list)  # Set of cities we need to visit.

    # Add the current city to the path and mark it as visited.
    path.append(start)
    visited.add(start)

    # If the current city is in the remaining cities to be visited, remove it.
    if start in remaining:
        city = graph.getCity(start)
        # for vehicle in vehicles:
            # city.update_population(city.population - vehicle.currentPeopleStock)
        remaining.remove(start)
    
    if start in supplier_list:
        for vehicle in vehicles:
            vehicle.currentPeopleStock = vehicle.maxPeopleHelped

    # Base case: If all cities in `end_list` have been visited, calculate the cost.
    if not remaining:
        # Calculate the total cost of the path.
        totalCostByVehicle = graph.pathCost(path, end_list, vehicles, 10000)  # Assuming 10000 people for calculation
        return path, totalCostByVehicle

    # Explore neighbors and continue searching recursively for each unvisited neighbor.
    for (neighbor, road) in graph.getNeighborsRoadPair(start):
        # Only visit neighbors that haven't been visited yet.
        if road.roadCondition == RoadConditions.DESTROYED:
            continue
        if neighbor not in visited:
            # Recursively visit the neighbors that haven't been visited yet.
            result = depthFirstSearch(
                graph, vehicles, neighbor, end_list, supplier_list, path[:], visited.copy(), remaining.copy()
            )
            if result:
                # If a valid path is found, return it.
                return result

    path.pop()  # Remove the last city from the path.

    # Return None if no valid path is found after backtracking.
    return None

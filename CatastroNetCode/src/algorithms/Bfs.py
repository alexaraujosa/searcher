from queue import Queue

from RoadConditions import RoadConditions


def breadthFirstSearch(graph, vehicles, start, end_list, supplier_list):
    """
    Breadth-First Search (BFS) algorithm to visit all cities in `end_list` starting from `start`.

    :param graph: The graph containing cities and roads.
    :param vehicles: List of vehicles available for travel.
    :param start: Starting city.
    :param end_list: List of cities to visit.
    :return: The path and total cost of visiting the cities in `end_list` or None if no valid path exists.
    """
    # Initialize the visited cities set and the BFS queue
    visited = set()
    queue = Queue()
    remaining = set(end_list)  # Set of cities that need to be visited
    people_in_need = 1000  # Example: Define the population from the first city

    # Add the start city to the queue and mark it as visited
    queue.put(start)
    visited.add(start)

    parent = dict()
    parent[start] = None

    path_found = False
    while not queue.empty() and remaining:
        current_city = queue.get()

        # If the current city is in the cities to be visited, remove it from remaining
        if current_city in remaining:
            remaining.remove(current_city)

        # Explore neighbors
        for (neighbor, road) in graph.getNeighborsRoadPair(current_city):
            # Don't explore destroyed roads
            if road.roadCondition == RoadConditions.DESTROYED:
                continue

            if neighbor not in visited:
                queue.put(neighbor)
                parent[neighbor] = current_city
                visited.add(neighbor)

        # Check if all cities in end_list have been visited
        if not remaining:
            path_found = True
            break

    # Reconstruct the path
    path = []
    if path_found:
        # Reconstruct the path from parent
        for city in end_list:
            if city in parent:
                current = city
                while current is not None:
                    path.append(current)
                    current = parent[current]
                path.reverse()

        print(path)
        # Calculate the total cost for all found paths
        totalCostByVehicle = graph.pathCost(path, end_list, vehicles, people_in_need)  # Assuming 10000 people for calculation
        return path, totalCostByVehicle

    return None, None
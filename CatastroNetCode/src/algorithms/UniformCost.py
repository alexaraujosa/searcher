import heapq

def uniformCost(graph, vehicles, start, end_list, supplier_list):
    """
    Perform Uniform Cost Search on a graph.

    Parameters:
        graph (dict): A dictionary where keys are nodes and values are lists of tuples (neighbor, cost).
        start: The starting node.
        goal: The goal node.

    Returns:
        tuple: (cost, path) where `cost` is the total cost to reach the goal, and `path` is the list of nodes forming the path.
               Returns (float('inf'), []) if the goal is unreachable.
    """
    #Aqui teriamos (Veiculo->{nome_cidadeObjetivo: (custo,caminho)})
    pathsByVehicle = {}

    for vehicle in vehicles:
        pathsByVehicle[vehicle.name] = {}
        pathToCity = {}

        for city_name in end_list:
            found = False
            priority_queue = [(0, start, [start])]
            # Set to track visited nodes
            visited = set()

            while priority_queue:
                # Pop the node with the smallest cost
                current_cost, current_city, path = heapq.heappop(priority_queue)

                # If we reach the goal, return the cost and path
                if current_city == city_name:
                    pathsByVehicle[vehicle.name][city_name] = (current_cost, path)
                    found = True
                    break

                # If the node has been visited, skip it
                if current_city in visited:
                    continue
                visited.add(current_city)

                # Explore neighbors
                for neighbor, road in graph.getNeighborsRoadPair(current_city):
                    if neighbor not in visited:
                        cost = graph.getRoadCost(vehicle, current_city, neighbor)
                        heapq.heappush(priority_queue, (current_cost + cost, neighbor, path + [neighbor]))

            # If the goal is not reachable
            if not found:
                pathsByVehicle[vehicle.name][city_name] = (float('inf'), [])

    return pathsByVehicle
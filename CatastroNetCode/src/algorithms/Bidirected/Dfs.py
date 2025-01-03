from time import sleep

from Graph import Graph
from RoadConditions import RoadConditions
from vehicles.Vehicle import Vehicle

def depthFirstSearch(graph, vehicles, start, end_list, supplier_list):
    """
    Perform Depth-First Search to find paths to multiple goal nodes.

    Parameters:
        graph: An object with a method `getNeighbors(node)` that returns neighbors of a node.
        start: The starting node.
        end_list: A list of goal nodes.

    Returns:
        dict: A dictionary where keys are goal nodes and values are paths (lists of nodes) to reach them.
              If a goal node is unreachable, its value will be an empty list.
    """
    pathsByGoal = {}

    for city in end_list:
        stack = [(start, [start])]
        visited = set()
        found = False

        while stack:
            current_city, path = stack.pop()

            if current_city == city:
                pathsByGoal[city] = path
                found = True
                break

            if current_city in visited:
                continue

            visited.add(current_city)

            for (neighbor, road) in graph.getNeighborsRoadPair(current_city):
                if road.roadCondition == RoadConditions.DESTROYED:
                    continue
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

        if not found:
            pathsByGoal[city] = []

    return pathsByGoal
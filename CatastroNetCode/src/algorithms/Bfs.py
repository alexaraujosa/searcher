from queue import Queue

from RoadConditions import RoadConditions


def breadthFirstSearch(graph, vehicles, start, end_list, supplier_list):
    """
        Perform Breadth-First Search to find paths to multiple goal nodes.

        Parameters:
            graph: An object with a method `getNeighbors(node)` that returns neighbors of a node.
            start: The starting node.
            end_list: A list of goal nodes.

        Returns:
            dict: A dictionary where keys are goal nodes and values are paths (lists of nodes) to reach them.
                  If a goal node is unreachable, its value will be an empty list.
        """
    from collections import deque

    pathsByGoal = {city: [] for city in end_list}
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_city, path = queue.popleft()

        # Mark as visited
        if current_city in visited:
            continue
        visited.add(current_city)

        # Check if this node is a goal
        for city in end_list:
            if current_city == city and not pathsByGoal[city]:
                pathsByGoal[city] = path

        # Add neighbors to the queue
        for neighbor in graph.getNeighbors(current_city):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return pathsByGoal
from collections import deque
from RoadConditions import RoadConditions


def breadthFirstSearchSinglePath(graph, vehicles, start, end_list, supplier_list):
    """
    Perform Breadth-First Search to find a path that includes all the goal cities exactly once.

    Parameters:
        graph: An object with a method `getNeighbors(node)` that returns neighbors of a node.
        start: The starting node.
        end_list: A list of goal nodes that must all be included in the path.

    Returns:
        list: A list containing the first path found that includes all the cities in end_list exactly once.
              If no such path is found, returns an empty list.
    """

    def bfs_recursive(graph, current_city, visited, path, remaining_goals, end_list):
        # If we've included all goal cities, return the current path
        if not remaining_goals:
            return path

        # Mark the current city as visited
        visited.add(current_city)

        # Explore neighbors
        for neighbor, road in graph.getNeighborsRoadPair(current_city):
            if road.roadCondition == RoadConditions.DESTROYED or neighbor in visited:
                continue

            # Add the neighbor to the path
            new_path = path + [neighbor]
            new_remaining_goals = remaining_goals.copy()

            # If the neighbor is a goal city, remove it from remaining goals
            if neighbor in end_list:
                new_remaining_goals.remove(neighbor)

            # Recursively explore with the updated state
            result = bfs_recursive(graph, neighbor, visited.copy(), new_path, new_remaining_goals, end_list)

            # If a valid path is found, return it
            if result:
                return result

        # If no valid path was found, backtrack and return None
        return None

    # Initialize the recursive BFS
    visited = set()
    path = [start]
    remaining_goals = set(end_list)
    result_path = bfs_recursive(graph, start, visited, path, remaining_goals, end_list)

    return result_path if result_path else []

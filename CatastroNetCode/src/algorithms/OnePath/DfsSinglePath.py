from time import sleep

from Graph import Graph
from RoadConditions import RoadConditions
from vehicles.Vehicle import Vehicle


def depthFirstSearchSinglePath(graph, vehicles, start, end_list, supplier_list):
    """
    Perform Depth-First Search (DFS) recursively to find the first path containing all cities from end_list.

    Parameters:
        graph: An object with a method `getNeighbors(node)` that returns neighbors of a node.
        start: The starting node.
        end_list: A list of goal nodes that must all be visited.

    Returns:
        list: The path (list of nodes) that contains all the cities in end_list.
              Returns an empty list if no such path is found.
    """
    # Helper function to perform DFS recursively
    def dfs(current_city, path, remaining):
        # Print the current city and the path being explored
        print(f"Exploring: {current_city} | Current Path: {path}")

        # If the current city is in the remaining cities to visit, remove it from the set
        if current_city in remaining:
            remaining.remove(current_city)

        # If there are no more cities left to visit, return the path
        if not remaining:
            print(f"Path Found: {path}")
            return path

        # Add all non-visited neighbors that aren't in destroyed roads
        for (neighbor, road) in graph.getNeighborsRoadPair(current_city):
            if road.roadCondition == RoadConditions.DESTROYED:
                continue
            if neighbor not in path:  # Avoid revisiting cities already in the path
                # Explore the next neighbor by recursively calling dfs
                new_path = path + [neighbor]
                new_remaining = remaining.copy()

                # Print the action of exploring the next city
                print(f"Exploring: {neighbor} from {current_city}")

                result = dfs(neighbor, new_path, new_remaining)
                if result:  # If we found a valid path, return it
                    return result

        # If no path has been found, backtrack by returning None
        print(f"Backtracking from: {current_city} | Current Path: {path}")
        return None

    # Start the DFS from the initial city
    return dfs(start, [start], set(end_list))
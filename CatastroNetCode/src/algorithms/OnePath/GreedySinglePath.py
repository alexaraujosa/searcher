from RoadConditions import RoadConditions

def greedySinglePath(graph, vehicles, start, end_list, supplier_list):
    """
    def greedy_recursive(graph, current_city, visited, path, remaining_goals, end_list):
        # If we've included all goal cities, return the current path
        if not remaining_goals:
            return path

        # Define a greedy criterion: prioritize neighbors that are closer to remaining goal cities
        best_neighbor = None
        best_distance = float('inf')

        # Explore neighbors to choose the one closest to any remaining goal city
        for neighbor, road in graph.getNeighborsRoadPair(current_city):
            if road.roadCondition == RoadConditions.DESTROYED or neighbor in visited:
                continue

            # Calculate heuristic: distance to the closest goal city
            heuristic = min([graph.getHeuristica(neighbor, goal) for goal in remaining_goals])

            # If this neighbor is better (greedy choice), update
            if heuristic < best_distance:
                best_distance = heuristic
                best_neighbor = neighbor

        # If no valid neighbor was found (dead-end), return None (backtrack)
        if best_neighbor is None:
            return None

        # Add the best neighbor to the path and update remaining goals
        new_path = path + [best_neighbor]
        new_remaining_goals = remaining_goals.copy()

        # If the neighbor is a goal city, remove it from remaining goals
        if best_neighbor in end_list:
            new_remaining_goals.remove(best_neighbor)

        # Mark the best neighbor as visited
        visited.add(best_neighbor)

        # Recursively explore with the updated state
        result = greedy_recursive(graph, best_neighbor, visited, new_path, new_remaining_goals, end_list)

        # If the path works, return it
        if result:
            return result

        # Backtrack: if the current path doesn't work, remove the neighbor and try the next one
        visited.remove(best_neighbor)

        # Try another neighbor (greedy approach won't stop, it will just pick others)
        return None

    # Initialize the greedy search
    visited = set()
    path = [start]
    remaining_goals = set(end_list)
    visited.add(start)  # Mark the start city as visited

    # Recursively try to find the first valid path
    result_path = greedy_recursive(graph, start, visited, path, remaining_goals, end_list)

    return result_path if result_path else []
    """
from City import City

from src.RoadConditions import RoadConditions


def aStarSearch(graph, vehicles, start, end_list, supplier_list):
    ret = {}

    # Initialize the result dictionary for each vehicle
    for v in vehicles:
        ret[v.name] = {}

    # Perform A* search for each vehicle
    for v in vehicles:
        for end in end_list:
            open_list = {start}
            closed_list = set([])

            g = {}
            g[start] = 0  # Cost from start to itself is zero

            parents = {}
            parents[start] = start  # The start node is its own parent

            # Initialize the result for this vehicle's goal city
            ret[v.name][end] = (0, [])  # (cost, path) - initialized with no cost and empty path

            while len(open_list) > 0:
                n = None

                # Find the node with the lowest f(n) = g(n) + h(n)
                for node in open_list:
                    if n is None or g[node] + graph.getHeuristica(node, end) < g[n] + graph.getHeuristica(n, end):
                        n = node

                # If no valid node is found, there is no path to the goal
                if n is None:
                    print(f'Path does not exist for vehicle {v.name} to goal {end}!')
                    return None

                # If the goal is reached, reconstruct the path
                if n == end:
                    cost, path = ret[v.name][end]
                    while parents[n] != n:  # Trace back from the goal to the start
                        cost += graph.getRoadCost(v, n, parents[n])  # Add road cost
                        path.append(n)  # Add the node to the path
                        n = parents[n]  # Move to the parent node
                    path.append(start)  # Add the start node to the path
                    path.reverse()  # Reverse to get the path from start to goal
                    ret[v.name][end] = (cost, path)  # Update the result with cost and path
                    break

                # Explore neighbors
                for m, road in graph.getNeighborsRoadPair(n):
                    if road.roadCondition == RoadConditions.DESTROYED:
                        continue
                    if m not in open_list and m not in closed_list:
                        open_list.add(m)
                        parents[m] = n
                        g[m] = g[n] + road.distance  # Add the cost of the road to reach m
                    else:
                        if g[m] > g[n] + road.distance:  # Found a better path to m
                            g[m] = g[n] + road.distance
                            parents[m] = n

                            # If m is in the closed list, move it back to the open list
                            if m in closed_list:
                                closed_list.remove(m)
                                open_list.add(m)

                open_list.remove(n)
                closed_list.add(n)

    return ret

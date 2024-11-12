import numpy as np
import random

def heuristic(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def probabilidade(neighbours, k_ant, currentCity, pheromone, alpha, beta):
    # Os vertices a serem visitados são os adjacentes? ou todos
    probabilities = []
    for i, neighbour in neighbours:
        h = heuristic(currentCity, neighbour)
        probabilities[i] = (pheromone[currentCity][neighbour] ** alpha) * (h ** beta)
    probabilities /= np.sum(probabilities)
    # Esta função escolhe um valor de neighbours em função da probabilidade de cada um, ou seja em função de p
    next_point = np.random.choice(neighbours, p=probabilities)
    return next_point

def ant_colony_optimization(cities, n_ants, n_iterations, alpha, beta, evaporation_rate, Q):
    n_cities = len(cities)
    pheromone = np.ones((n_cities, n_cities))
    best_path = None
    best_path_length = np.inf

    for iteration in range(n_iterations):
        paths = []
        path_lengths = []

        for ant in range(n_ants):
            visited = [False] * n_cities
            current_point = np.random.randint(n_cities)
            visited[current_point] = True
            path = [current_point]
            path_length = 0

            while False in visited:
                unvisited = np.where(np.logical_not(visited))[0]
                probabilities = np.zeros(len(unvisited))

                for i, unvisited_point in enumerate(unvisited):
                    # Neste algoritmo ele divide o valor das feromonas com a distancia... isto está bem?
                    # As cidades que devemos ter em conta para o total sao as adjacentes? ou todas?
                    probabilities[i] = pheromone[current_point, unvisited_point] ** alpha / heuristic(
                        cities[current_point], cities[unvisited_point]) ** beta

                probabilities /= np.sum(probabilities)

                next_point = np.random.choice(unvisited, p=probabilities)
                path.append(next_point)
                path_length += heuristic(cities[current_point], cities[next_point])
                visited[next_point] = True
                current_point = next_point

            paths.append(path)
            path_lengths.append(path_length)

            if path_length < best_path_length:
                best_path = path
                best_path_length = path_length

        pheromone *= evaporation_rate

        for path, path_length in zip(paths, path_lengths):
            for i in range(n_cities - 1):
                pheromone[path[i], path[i + 1]] += Q / path_length
            pheromone[path[-1], path[0]] += Q / path_length

# Example usage:
points = np.random.rand(10, 3)  # Generate 10 random 3D points
ant_colony_optimization(points, n_ants=10, n_iterations=100, alpha=1, beta=1, evaporation_rate=0.5, Q=1)
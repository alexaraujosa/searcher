# Classe grafo para representaçao de grafos,
import csv
import os
import random

from shapely.measurement import distance

from Road import *
import math
from queue import Queue

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem
from networkx.classes import nodes, neighbors

from City import City
from RoadConditions import RoadConditions




class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = {}
        self.size = len(self.nodes)


    def load(self, filename= '../data/graph_data.csv'):
        self.graph = {}
        self.nodes = {}

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        city1_name = row['Município 1']
                        city2_name = row['Município 2']
                        distance = float(row['Distancia (km)']) if row['Distancia (km)'] != 'N/A' else None
                        pop1 = int(row['População 1'])
                        pop2 = int(row['População 2'])
                        lon1, lat1 = float(row['Pos_X 1']), float(row['Pos_Y 1'])
                        lon2, lat2 = float(row['Pos_X 2']), float(row['Pos_Y 2'])

                        city1 = City(city1_name, pop1, lon1, lat1)
                        city2 = City(city2_name, pop2, lon2, lat2)

                        road = Road(distance, RoadConditions.NORMAL)

                        if city1_name not in self.nodes:
                            self.nodes[city1_name] = city1
                            self.graph[city1_name] = []

                        if city2_name not in self.nodes:
                            self.nodes[city2_name] = city2
                            self.graph[city2_name] = []

                        if distance is not None:
                            if not self.isNeighbor(city1_name, city2_name):
                                self.graph[city1_name].append((city2_name, road))

                            if not self.isNeighbor(city2_name, city1_name):
                                self.graph[city2_name].append((city1_name, road))

                    except ValueError as e:
                        print(f"Error processing row {row}: {e}")

        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
        except PermissionError:
            print(f"Error: Permission denied to read the file {filename}.")
        except Exception as e:
            print(f"Unexpected error occurred while loading the graph: {e}")

        print(f"\033[32mGrafo carregado com {len(self.nodes)} nós e {sum(len(v) for v in self.graph.values()) // 2} arestas.\033[0m")

    def getNeighbors(self, city_name):
        neighbors = []

        for (neighbor_name, road) in self.graph[city_name]:
            neighbors.append(neighbor_name)
        return neighbors

    def getNeighborsRoadPair(self, city_name):
        return self.graph[city_name]

    def isNeighbor(self, city1_name, city2_name):
        for neighbor, _ in self.graph[city1_name]:
            if neighbor == city2_name:
                return True
        return False

    def getCity(self, city_name):
        if city_name in self.nodes:
            return self.nodes[city_name]
        else:
            return None

    def getRoadBetween(self, city1_name, city2_name):
        road = None

        for (neighbor,road) in self.getNeighborsRoadPair(city1_name):
            if neighbor == city2_name:
                road = road
                break

        return road

    def randomizeRoadConditions(self, cities_to_randomize=None, change_probability=0.2):
        """
        Randomiza as condições das estradas, mas apenas para algumas cidades selecionadas.

        :param cities_to_randomize: Lista de cidades para as quais as estradas serão randomizadas.
                                    Se None, escolhe aleatoriamente algumas cidades.
        :param change_probability: Probabilidade de uma estrada entre duas cidades ter sua condição alterada.
        """
        # Se não foi especificada uma lista de cidades, escolhemos aleatoriamente algumas cidades do grafo
        if not cities_to_randomize:
            cities_to_randomize = random.sample(list(self.nodes.keys()), k=int(len(self.nodes) * 0.3))# Randomiza 30% das cidades

        # Iterar por todas as cidades que queremos randomizar
        for city_name in cities_to_randomize:
            for neighbor_name, road in self.graph[city_name]:
                # Com base na probabilidade, decidimos se alteramos a condição da estrada
                if random.random() < change_probability:
                    # Randomiza a condição da estrada
                    new_condition = random.choice(list(RoadConditions))
                    self.changeRoadCondition(city_name, neighbor_name, new_condition)
                    #print(f"Road condition between {city_name} and {neighbor_name} changed to {new_condition}.")

    def changeRoadCondition(self, city1_name, city2_name, roadCondition):
        """
        Altera a condição de uma estrada entre duas cidades.
        """
        for (neighbor, road) in self.graph[city1_name]:
            if neighbor == city2_name:
                road.updateRoadCondition(roadCondition)
                #print(f"Weather condition between {city1_name} and {city2_name} changed to {roadCondition}.")
                return

        #print(f"No direct road found between {city1_name} and {city2_name}.")
        return


    ######################################
    #    escrever o grafo como string    #
    ######################################
    def printGraph(self):
        if self.size == 0:
            print("Graph is not loaded.")

        for city1 in self.graph.keys():
            print(f"{city1}: {self.graph[city1]}")
        # for city in self.nodes:
            # print(self.nodes[city])

        ################################
        #   Guardar o grafo como png
        ################################
        def saveCurrentGraphAsPNG(self):
            # Get the number of files in the images folder
            nFiles = int(len(os.listdir('../images/')) // 2)

            # Define filenames
            labeled_filename = f"../images/grafo_municipios_labeled{nFiles}.png"
            semi_labeled_filename = f"../images/grafo_municipios_semi_labeled{nFiles}.png"
            dots_filename = f"../images/grafo_municipios_dots{nFiles}.png"

            # Create a NetworkX graph object
            G = nx.Graph()

            # Add nodes to the NetworkX graph
            for city_name, city in self.nodes.items():
                G.add_node(city_name, pos=(city.longitude, city.latitude))

            # Add edges to the NetworkX graph and associate road conditions with edges
            for city_name, neighbors in self.graph.items():
                for neighbor_name, road in neighbors:
                    G.add_edge(city_name, neighbor_name, weight=road.distance, road_condition=road.roadCondition)

            # Extract node positions
            pos = nx.get_node_attributes(G, 'pos')

            # Assign colors to edges based on RoadConditions
            edge_colors = []
            for u, v, data in G.edges(data=True):
                road_condition = data[
                    'road_condition']  # Assuming road_condition is an enum or string like 'NORMAL', 'STORM'

                # Define colors based on the RoadCondition (example logic)
                if road_condition == RoadConditions.DESTROYED:
                    edge_colors.append('red')  # Red for storm
                elif road_condition == RoadConditions.NORMAL:
                    edge_colors.append('green')  # Green for normal conditions
                elif road_condition == RoadConditions.FLOOD:
                    edge_colors.append('blue')
                elif road_condition == RoadConditions.STORM:
                    edge_colors.append('yellow')
                else:
                    edge_colors.append('gray')  # Default color for other conditions

            # First plot: Full graph with labels and distances
            plt.figure(figsize=(20, 20))  # Scale figure size for clarity
            nx.draw(G, pos, with_labels=True, node_size=40, font_size=8, node_color='skyblue', font_color='black',
                    edge_color=edge_colors)

            # Add edge labels for distances
            edge_labels = nx.get_edge_attributes(G, 'weight')
            edge_labels = {(u, v): f"{int(data)} km" for (u, v), data in edge_labels.items()}  # Corrected line
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

            plt.title("Portugal Municipal Graph (Geographical Proportions)")
            plt.savefig(labeled_filename, dpi=200)
            plt.show()
            print(f"Graph with labels saved to {labeled_filename}")

            # Second plot: Full graph with labels only
            plt.figure(figsize=(20, 20))  # Scale figure size for clarity
            nx.draw(G, pos, with_labels=True, node_size=40, font_size=8, node_color='skyblue', font_color='black',
                    edge_color=edge_colors)

            plt.title("Names Only - Portugal Municipal Graph (Geographical Proportions)")
            plt.savefig(semi_labeled_filename, dpi=200)
            plt.show()
            print(f"Graph with semi labels saved to {semi_labeled_filename}")

            # Third plot: Minimalist graph with dots only
            plt.figure(figsize=(20, 20))
            nx.draw(G, pos, with_labels=False, node_size=10, node_color='blue', edge_color=edge_colors)

            plt.title("Nodes Only - Portugal Municipal Graph (Geographical Proportions)")
            plt.savefig(dots_filename, dpi=200)
            plt.show()
            print(f"Graph with dots only saved to {dots_filename}")

        def saveRouteAsPNG(self, path, end_list):
            """
            Save an image of the graph with the path found by DFS highlighted in green,
            and cities in end_list highlighted in red.

            :param path: The path list from DFS that contains the cities in order.
            :param end_list: List of cities that need to be visited and should be colored red.
            """
            # Get the number of files in the images folder
            nFiles = int(len(os.listdir('../routes/')))

            # Define filenames
            route_filename = f"../routes/route{nFiles}.png"

            # Create a NetworkX graph object
            G = nx.Graph()

            # Add nodes to the NetworkX graph
            for city_name, city in self.nodes.items():
                G.add_node(city_name, pos=(city.longitude, city.latitude))

            # Add edges to the NetworkX graph
            for city_name, neighbors in self.graph.items():
                for neighbor_name, road in neighbors:
                    G.add_edge(city_name, neighbor_name, weight=road.distance)

            # Extract node positions
            pos = nx.get_node_attributes(G, 'pos')

            # Draw the full graph in black
            plt.figure(figsize=(20, 20))  # Scale figure size for clarity
            nx.draw(
                G, pos, with_labels=True, node_size=40, font_size=8,
                node_color='skyblue', font_color='black', edge_color='black'
            )

            # Overlay the path in green
            path_edges = [
                (path[i], path[i + 1])
                for i in range(len(path) - 1)
                if G.has_edge(path[i], path[i + 1])
            ]
            nx.draw_networkx_edges(
                G, pos, edgelist=path_edges, edge_color='green', width=2
            )

            # Highlight nodes in end_list in red
            end_nodes = [node for node in end_list if node in G.nodes()]
            nx.draw_networkx_nodes(
                G, pos, nodelist=end_nodes, node_color='red', node_size=80
            )

            # Save and show the final graph
            plt.title("Graph with Full View (Black) and Path Highlighted (Green)")
            plt.savefig(route_filename, dpi=200)
            plt.show()
            print(f"Graph with highlighted path and end cities saved to {route_filename}")

    ##############################3
    #   imprimir arestas
    ############################333333

    ################
    #   adicionar   aresta no grafo
    ######################

    #############################
    # devolver nodos
    ##########################

    #######################
    #    devolver o custo de uma aresta
    ##############
    def getRoadCost(self, vehicle, city1_name, city2_name):
        road = self.getRoadBetween(city1_name, city2_name)
        distance = road.distance

        if road.roadCondition == RoadConditions.DESTROYED:
            return float('inf')

        if road is None:
            print(f"No road found between {city1_name} and {city2_name}.")

        if vehicle.name == 'Helicopter':
            distance = self.getCity(city1_name).distance_to(self.getCity(city2_name))

        vehiclePenalty = vehicle.getVehiclePenalty(road.roadCondition)
        travelTime = vehicle.getTravelTime(distance)
        fuelNeeded = vehicle.getFuelNeeded(distance)

        return (vehiclePenalty * travelTime) + fuelNeeded



    ##############################
    #  dado um caminho calcula o seu custo
    ###############################
    def pathCost(self, path, end_list, vehicleList, peopleInNeed):
        vehicleCost = {}

        for vehicle in vehicleList:
            custo = 0
            i = 0

            match vehicle.name:
                case 'Helicopter' | 'Drone':
                    lastLocation = path[0]
                    while i < len(path):
                        if path[i] in end_list:
                            custo += self.getRoadCost(vehicle, lastLocation, path[i])
                            lastLocation = path[i]
                        i += 1
                case 'Truck' | 'Boat':
                    while i + 1 < len(path):
                        custo += self.getRoadCost(vehicle, path[i], path[i + 1])
                        i += 1
                case _:
                    print(f"Unknown vehicle type: {vehicle.name}")
                    continue

#vehicleCost[vehicle.name] = round(custo * (1 + (peopleInNeed / vehicle.maxPeopleHelped)))
            vehicleCost[vehicle.name] = custo#round(custo * (1 + (peopleInNeed / vehicle.maxPeopleHelped)))

        return vehicleCost

    ########################################
    # função que devolve vizinhos de um nó
    ########################################

    ##################################
    #    add_heuristica   -> define heuristica para cada nodo 1 por defeito....
    ##########################################

    #################################
    # devolve heuristica do nodo
    #################################
    def getHeuristica(self, start, end):
        start_city = self.getCity(start)
        end_city = self.getCity(end)
        if not start_city or not end_city:
            return
        return start_city.distance_to(end_city)

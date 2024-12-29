# Classe grafo para representaçao de grafos,
import csv
import math
from queue import Queue

import networkx as nx  # biblioteca de tratamento de grafos necessária para desnhar graficamente o grafo
import matplotlib.pyplot as plt  # idem
from networkx.classes import nodes

from City import City

class Graph:
    # def __init__(self, num_of_nodes, directed=False):
    def __init__(self):
        self.graph = {}
        self.nodes = []
        self.size = self.nodes.__len__()


    def load(self, filename):
        self.graph = {}
        self.nodes = []

        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                city1_name = row['Município 1']
                city2_name = row['Município 2']
                distance = float(row['Distancia (km)']) if row['Distancia (km)'] != 'N/A' else None
                EucliadianDistance = float(row['Distancia Euclidiana']) if row['Distancia Euclidiana'] != 'N/A' else None
                pop1 = int(row['População 1'])
                pop2 = int(row['População 2'])
                lon1, lat1 = float(row['Pos_X 1']), float(row['Pos_Y 1'])
                lon2, lat2 = float(row['Pos_X 2']), float(row['Pos_Y 2'])

                city1 = City(city1_name, pop1, lon1, lat1)
                city2 = City(city2_name, pop2, lon2, lat2)

                if city1 not in self.nodes:
                    self.nodes.append(city1)
                    self.graph[city1_name] = []

                if city2 not in self.nodes:
                    self.nodes.append(city2)
                    self.graph[city2_name] = []

                if distance is not None:
                    self.graph[city1_name].append((city2_name, (distance, EucliadianDistance)))

        print(f"\033[32mGrafo carregado com {len(self.nodes)} nós e {sum(len(v) for v in self.graph.values()) // 2} arestas.\033[0m")

    #############
    #    escrever o grafo como string
    #############

    ################################
    #   encontrar nodo pelo nome
    ################################

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
    ##############3

    ##############################
    #  dado um caminho calcula o seu custo
    ###############################

    ####################
    # função que devolve vizinhos de um nó
    ##############################

    ###########################
    # desenha grafo  modo grafico
    #########################

    ####################################33
    #    add_heuristica   -> define heuristica para cada nodo 1 por defeito....
    ################################3

    ###################################3
    # devolve heuristica do nodo
    ####################################

graph = Graph()
graph.load("../data/graph_data.csv")

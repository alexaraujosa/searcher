# Classe city para definição dos nós do grafo (Cidades)
import math

class Road:
    def __init__(self, distance, roadCondition):
        # Inicializa os atributos da cidade
        self.distance = distance
        self.roadCondition = roadCondition

    def updateDistance(self, distance):
        # Atualiza a população da cidade
        self.distance = distance

    def updateRoadCondition(self, roadCondition):
        self.roadCondition = roadCondition

    def __str__(self):
        # Método para mostrar uma representação textual da cidade
        return f"Distancia-> {self.distance} Km || Condição Atual-> {self.roadCondition}"

    def __repr__(self):
        # Método para mostrar uma representação textual da cidade
        return f"({self.distance} Km || {self.roadCondition})"

    def __eq__(self, other):
        if not isinstance(other, Road):
            return False
        return self.distance == other.distance and self.roadCondition == other.roadCondition

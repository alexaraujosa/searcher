# Classe city para definição dos nós do grafo (Cidades)
import math

class City:
    def __init__(self, name, population, longitude, latitude):
        # Inicializa os atributos da cidade
        self.name = str(name)
        self.population = int(population)
        self.longitude = float(longitude)
        self.latitude = float(latitude)

    def __str__(self):
        # Método para mostrar uma representação textual da cidade
        return f"Name-> {self.name} || Population-> {self.population}"

    def get_coordinates(self):
        # Retorna as coordenadas geográficas (longitude, latitude)
        return self.longitude, self.latitude

    def update_population(self, new_population):
        # Atualiza a população da cidade
        self.population = int(new_population)

    def is_critical(self, threshold):
        # Verifica se a cidade tem uma população maior que o limite
        return self.population > threshold

    def distance_to(self, other_city):
        # Raio da Terra em km
        R = 6371.0

        # Obtém as coordenadas das duas cidades
        lon1, lat1 = self.get_coordinates()
        lon2, lat2 = other_city.get_coordinates()

        # Converte as coordenadas de graus para radianos
        lon1, lat1 = math.radians(lon1), math.radians(lat1)
        lon2, lat2 = math.radians(lon2), math.radians(lat2)

        # Fórmula de Haversine
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Distância em km
        distance = R * c
        return distance

    def __eq__(self, other):
        if not isinstance(other, City):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
import math
import networkx as nx
import csv
import matplotlib.pyplot as plt
import requests
import osmnx as ox
import json

def get_municipios_from_region(region_name):
    """
    Consulta os municípios (admin_level=7) de uma região no OpenStreetMap usando OSMnx
    e também lê um arquivo JSON que contém dados sobre a população e outros detalhes
    dos municípios. Combina as informações e retorna um DataFrame com os dados completos.
    """
    try:
        municipios_osmnx = ox.features_from_place(
            region_name,
            tags={"admin_level": "7", "boundary": "administrative"}
        )

        # Filtra para incluir apenas polígonos de municípios (caso existam)
        municipios_osmnx = municipios_osmnx[municipios_osmnx.geometry.type == 'Polygon']
        municipios_osmnx = municipios_osmnx[municipios_osmnx.border_type == 'município']
        municipios_osmnx = municipios_osmnx.drop_duplicates(subset='name')

        return municipios_osmnx

    except Exception as e:
        print(f"Erro ao consultar ou processar os dados: {e}")
        return None


def save_population_data_from_query(file_name="../data/OSMinfo.json"):
    """
    Consulta a população dos municípios de Portugal Continental usando a Overpass API
    e salva a resposta da consulta como um arquivo JSON.
    """
    overpass_url = "http://overpass-api.de/api/interpreter"

    # Consulta Overpass para encontrar os municípios de Portugal Continental
    query = """
    [out:json];
    area["name"="Portugal"]["boundary"="administrative"];
    relation["boundary"="administrative"]["admin_level"="7"]["border_type"="município"](area);
    out tags;
    """

    # Realiza a consulta
    response = requests.get(overpass_url, params={'data': query})

    # Verifica se a consulta foi bem-sucedida
    if response.status_code == 200:
        data = response.json()  # Dados da consulta

        # Salva o JSON gerado em um arquivo com codificação UTF-8
        with open(file_name, "w", encoding='utf-8') as f:  # Força a codificação UTF-8
            json.dump(data, f, indent=4, ensure_ascii=False)  # Salva com formatação legível e preserva caracteres especiais
        print(f"Arquivo JSON salvo como {file_name}")
    else:
        print(f"Erro na consulta: {response.status_code}")


def create_population_dict_from_json(file_name="OSMinfo.json"):
    """
    Cria um dicionário com os nomes dos municípios e suas populações a partir de um arquivo JSON.

    :param file_name: Nome do arquivo JSON com os dados de população dos municípios.
    :return: Dicionário com nome do município como chave e a população como valor.
    """
    municipios_combined = {}  # Dicionário que será preenchido

    try:
        # Abrir o arquivo JSON para leitura
        with open(file_name, "r", encoding="utf-8") as f:
            data = json.load(f)  # Carregar os dados do JSON

            # Verificar se a chave 'elements' existe nos dados
            if 'elements' not in data:
                print(f"Erro: O formato do arquivo {file_name} está incorreto.")
                return None

            # Processar cada elemento da lista 'elements' e preencher o dicionário
            for element in data.get('elements', []):
                municipio_name = element['tags'].get('name')  # Nome do município
                population = element['tags'].get('population', 'N/A')  # População do município

                # Se o nome do município existir, adiciona ao dicionário
                if municipio_name:
                    municipios_combined[municipio_name] = population

        # Exibe o dicionário gerado
        print(f"Dicionário de populações carregado. Total de municípios: {len(municipios_combined)}")
        return municipios_combined  # Retorna o dicionário

    except json.JSONDecodeError as e:
        print(f"Erro ao ler o arquivo JSON: {e}")
        return None
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None

# Função para gerar o grafo
def generate_graph_from_municipios(municipios_combined, G_roads):
    # Projeta o grafo de ruas
    G = nx.Graph()

    for idx, row in municipios_combined.iterrows():
        municipio_name = row["name"]
        if municipio_name not in G:
            G.add_node(municipio_name, geometry=row["geometry"])

        # Verificar geometria e calcular o centroide
        if not row["geometry"].is_valid:
            row["geometry"] = row["geometry"].buffer(0)

        if row["geometry"].geom_type == "MultiPolygon":
            centroid = row["geometry"].convex_hull.centroid
        else:
            centroid = row["geometry"].centroid

        # Encontrar nó mais próximo
        nearest_node = ox.distance.nearest_nodes(G_roads, centroid.x, centroid.y)
        G.nodes[municipio_name]['nearest_node'] = nearest_node

    # Identificar os vizinhos usando interseções de fronteiras
    for i, row_i in municipios_combined.iterrows():
        for j, row_j in municipios_combined.iterrows():
            if i != j and row_i["geometry"].touches(row_j["geometry"]):
                node_i = G.nodes[row_i["name"]]['nearest_node']
                node_j = G.nodes[row_j["name"]]['nearest_node']

                if nx.has_path(G_roads, node_i, node_j):
                    try:
                        distance = nx.shortest_path_length(G_roads, node_i, node_j, weight='length') / 1000
                        if distance > 0:  # Only add edges with valid distances
                            G.add_edge(row_i["name"], row_j["name"], weight=distance)
                    except Exception as e:
                        print(f"Error calculating distance between {row_i['name']} and {row_j['name']}: {e}")

    return G


def haversine(lat1, lon1, lat2, lon2):
    """
    Calcula a distância em quilômetros entre dois pontos na superfície da Terra
    usando a fórmula de Haversine.

    :param lat1: Latitude do primeiro ponto.
    :param lon1: Longitude do primeiro ponto.
    :param lat2: Latitude do segundo ponto.
    :param lon2: Longitude do segundo ponto.
    :return: Distância em quilômetros entre os dois pontos.
    """
    # Raio da Terra em quilômetros
    R = 6371.0

    # Converter as coordenadas de graus para radianos
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Diferenças das coordenadas
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Fórmula de Haversine
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distância em quilômetros
    distance = R * c
    return distance

def save_data_csv(G, dic_municipios_population, output_filename="../data/graph_data.csv"):
    """
    Salva as informações do grafo, incluindo as distâncias reais entre os municípios,
    as populações dos municípios e suas coordenadas, em um arquivo CSV, garantindo
    que o arquivo seja bidirecional (se há uma aresta de A para B, também terá de haver
    uma de B para A).

    :param G: Grafo de municípios.
    :param dic_municipios_population: Dicionário com a população dos municípios.
    :param output_filename: Nome do arquivo de saída.
    """
    # Abrir o arquivo para escrita
    with open(output_filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Cabeçalhos do arquivo
        writer.writerow(["Município 1", "Município 2", "Distancia (km)", "Distancia Euclidiana", "População 1", "População 2", "Pos_X 1", "Pos_Y 1", "Pos_X 2", "Pos_Y 2"])

        # Criar um conjunto para garantir que cada aresta seja escrita apenas uma vez
        written_edges = set()

        # Iterar sobre as arestas do grafo
        for municipio_1, municipio_2, edge_data in G.edges(data=True):
            # Garantir que a aresta não foi escrita ainda (bidirecional)
            edge_pair = frozenset([municipio_1, municipio_2])
            if edge_pair in written_edges:
                continue
            written_edges.add(edge_pair)

            # Recuperar dados dos dois municípios
            pop_1 = dic_municipios_population.get(municipio_1, "N/A")
            pop_2 = dic_municipios_population.get(municipio_2, "N/A")

            # Recuperar as coordenadas (latitude e longitude) dos dois municípios
            lat_1 = G.nodes[municipio_1]['geometry'].centroid.y  # latitude
            lon_1 = G.nodes[municipio_1]['geometry'].centroid.x  # longitude
            lat_2 = G.nodes[municipio_2]['geometry'].centroid.y  # latitude
            lon_2 = G.nodes[municipio_2]['geometry'].centroid.x  # longitude

            # Distância real (Haversine) entre os dois municípios
            dist_real = haversine(lat_1, lon_1, lat_2, lon_2)

            # Arredondar a distância real para inteiro
            dist_real_arredondada = round(dist_real)

            # Distância da aresta (peso)
            distancia_aresta = edge_data.get('weight', "N/A")

            distancia_aresta_arredondada  = round(distancia_aresta)

            # Escrever linha no CSV para essa aresta (municipio_1 -> municipio_2)
            writer.writerow([municipio_1, municipio_2, distancia_aresta_arredondada, dist_real_arredondada, pop_1, pop_2, lon_1, lat_1, lon_2, lat_2])

            # Escrever linha no CSV para a aresta invertida (municipio_2 -> municipio_1)
            writer.writerow([municipio_2, municipio_1, distancia_aresta_arredondada, dist_real_arredondada, pop_2, pop_1, lon_2, lat_2, lon_1, lat_1])

    print(f"Dados salvos no arquivo: {output_filename}")


# Função para visualizar e salvar a imagem do grafo com disposição geográfica
def plot_and_save_graph(G, labeled_filename="../images/grafo_municipios_labeled.png", dots_filename="../images/grafo_municipios_dots.png"):
    """
    Visualize and save graphs:
    1. Full labeled graph with geographical proportions.
    2. Graph with nodes only (dots) for a minimal visualization.
    """
    # Extract node positions based on geographical coordinates
    pos = {node: (G.nodes[node]['geometry'].centroid.x, G.nodes[node]['geometry'].centroid.y) for node in G.nodes}

    # First plot: Full graph with labels and distances
    plt.figure(figsize=(20, 20))  # Scale figure size for clarity
    nx.draw(G, pos, with_labels=True, node_size=40, font_size=8, node_color='skyblue', font_color='black')

    # Add edge labels for distances
    edge_labels = {
        (u, v): f"{int(data['weight'])} km"
        for u, v, data in G.edges(data=True) if 'weight' in data
    }
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title("Grafo de Municípios de Portugal (Geographical Proportions)")
    plt.savefig(labeled_filename, dpi=300)
    plt.show()
    print(f"Graph with labels saved to {labeled_filename}")

    # Second plot: Minimalist graph with dots only
    plt.figure(figsize=(20, 20))
    nx.draw(G, pos, with_labels=False, node_size=10, node_color='blue')

    plt.title("Nodes Only - Grafo de Municípios (Geographical Proportions)")
    plt.savefig(dots_filename, dpi=300)
    plt.show()
    print(f"Graph with dots only saved to {dots_filename}")


def run():
    # Salvar os dados de população usando a consulta Overpass
    print("\033[33m A adquirir a informação do OSM usando overpasss api...\033[0m")
    save_population_data_from_query("../data/OSMinfo.json")

    # Criar o dicionário de populações a partir do arquivo JSON gerado
    print("\n\033[33m A gerar o dicionario com par chave valor (nome do municipio->população)...\033[0m")
    municipios_population = create_population_dict_from_json("../data/OSMinfo.json")

    # Definir a rede viária para o país inteiro
    print("\n\033[33m A adquirir a rede rodoviaria de portugal continental...\033[0m")
    place_name = "Portugal Continental"
    G_roads = ox.graph_from_place(place_name, network_type='drive',
                                    custom_filter='["highway"~"motorway|trunk|primary"]')

    # Definir as fornteira dos municipios e adquir informação geografica dos mesmos
    print("\n\033[33m A adquirir informação geográfica do vários municipios...\033[0m")
    municipios_combined = get_municipios_from_region(place_name)

    i = 0
    if 'name' in municipios_combined.columns:
        for name in municipios_combined['name']:
            i = i+1
    else:
        print("The GeoDataFrame does not contain a 'name' column.")
    print("\n\033[32m Serão usados "+ str(i) +" municipios para representar o grafo de portugal ...\033[0m")


    # Gerar o grafo
    print("\n\033[33m A criar o grafo de Portugal...\033[0m")
    G = generate_graph_from_municipios(municipios_combined, G_roads)

    print("\n\033[33m A gerar o csv com a informação necessária a replicação do grafo...\033[0m")
    save_data_csv(G, municipios_population)

    # Salvar a imagem do grafo com disposição geográfica
    print("\n\033[33m A guardar imagems...\033[0m")
    plot_and_save_graph(G)

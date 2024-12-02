from tqdm import tqdm
import os
import osmnx as ox
import geopandas as gpd
import networkx as nx
import pandas as pd
import time
import matplotlib.pyplot as plt



municipios_continentais = [
    "Abrantes", "Águeda", "Albergaria-a-Velha", "Albufeira", "Alcácer do Sal", "Alcanena",
    "Alcobaça", "Alcochete", "Alcoutim", "Alenquer", "Alfândega da Fé", "Alijó", "Aljezur",
    "Almada", "Almeida", "Almeirim", "Almodôvar", "Alpiarça", "Alter do Chão", "Alvaiázere",
    "Amadora", "Amarante", "Amares", "Ansião", "Arcos de Valdevez", "Arganil", "Armamar",
    "Arouca", "Arraiolos", "Arronches", "Arruda dos Vinhos", "Aveiro", "Avis", "Azambuja",
    "Baião", "Barcelos", "Barrancos", "Barreiro", "Batalha", "Beja", "Belmonte", "Benavente",
    "Bombarral", "Borba", "Boticas", "Braga", "Bragança", "Cabeceiras de Basto", "Cadaval",
    "Caldas da Rainha", "Calheta de São Jorge", "Caminha", "Campo Maior", "Cantanhede",
    "Carrazeda de Ansiães", "Carregal do Sal", "Cartaxo", "Cascais", "Castanheira de Pera",
    "Castelo Branco", "Castelo de Paiva", "Castelo de Vide", "Castro Daire", "Castro Marim",
    "Castro Verde", "Celorico da Beira", "Celorico de Basto", "Chamusca", "Chaves", "Cinfães",
    "Constância", "Coruche", "Covilhã", "Crato", "Cuba", "Elvas", "Entroncamento", "Espinho",
    "Esposende", "Estarreja", "Estremoz", "Évora", "Ferreira do Alentejo", "Ferreira do Zêzere",
    "Figueira da Foz", "Figueira de Castelo Rodrigo", "Figueiró dos Vinhos", "Freixo de Espada à Cinta",
    "Fronteira", "Gavião", "Góis", "Gondomar", "Gouveia", "Grândola", "Guarda", "Guimarães",
    "Idanha-a-Nova", "Ílhavo", "Lagoa (Algarve)", "Lagos", "Lamego", "Leiria", "Lourinhã",
    "Lousã", "Lousada", "Loures", "Loulé", "Mação", "Macedo de Cavaleiros", "Mafra", "Maia",
    "Mangualde", "Manteigas", "Marco de Canaveses", "Marinha Grande", "Marvão", "Matosinhos",
    "Mealhada", "Mêda", "Melgaço", "Mértola", "Mesão Frio", "Mira", "Miranda do Corvo",
    "Miranda do Douro", "Mirandela", "Mogadouro", "Moimenta da Beira", "Moita", "Monção",
    "Monchique", "Mondim de Basto", "Monforte", "Montalegre", "Montemor-o-Novo",
    "Montemor-o-Velho", "Montijo", "Mora", "Mortágua", "Moura", "Mourão", "Nazaré", "Nelas",
    "Nisa", "Óbidos", "Odemira", "Odivelas", "Oeiras", "Olhão", "Oliveira de Azeméis",
    "Oliveira de Frades", "Oliveira do Bairro", "Oliveira do Hospital", "Ourém", "Ourique",
    "Pampilhosa da Serra", "Palmela", "Paredes", "Paredes de Coura", "Pedrógão Grande",
    "Penacova", "Penafiel", "Penalva do Castelo", "Penamacor", "Penedono", "Penela",
    "Peso da Régua", "Pinhel", "Pombal", "Ponte de Lima", "Portalegre", "Portimão",
    "Porto", "Porto de Mós", "Proença-a-Nova", "Redondo", "Reguengos de Monsaraz",
    "Resende", "Rio Maior", "Sabrosa", "Sabugal", "Salvaterra de Magos", "Santa Comba Dão",
    "Santa Maria da Feira", "Santarém", "Santiago do Cacém", "Santo Tirso",
    "São Brás de Alportel", "São João da Madeira", "São Pedro do Sul", "Sardoal", "Sátão",
    "Seia", "Seixal", "Sernancelhe", "Serpa", "Sertã", "Sesimbra", "Setúbal",
    "Sever do Vouga", "Silves", "Sines", "Sintra", "Sobral de Monte Agraço", "Soure",
    "Sousel", "Tábua", "Tabuaço", "Tarouca", "Tavira", "Terras de Bouro", "Tomar",
    "Tondela", "Torre de Moncorvo", "Torres Novas", "Torres Vedras", "Trancoso",
    "Trofa", "Vagos", "Vale de Cambra", "Valença", "Valongo", "Valpaços",
    "Vendas Novas", "Viana do Alentejo", "Viana do Castelo", "Vidigueira", "Vieira do Minho",
    "Vila de Rei", "Vila do Conde", "Vila Flor", "Vila Franca de Xira", "Vila Nova de Cerveira",
    "Vila Nova de Famalicão", "Vila Nova de Foz Côa", "Vila Nova de Gaia",
    "Vila Pouca de Aguiar", "Vila Real", "Vila Velha de Ródão", "Viseu", "Vizela", "Vouzela"
]




# Função para obter os municípios de uma região
def get_municipios_from_region(region_name):
    """
    Consulta os municípios (admin_level=8) de uma região no OpenStreetMap.
    """
    try:
        municipios = ox.features_from_place(
            region_name,
            tags={"admin_level": "7", "boundary": "administrative", "border_type": "município"}
        )
        municipios = municipios[municipios.geometry.type == 'Polygon']
        return municipios
    except Exception as e:
        print(f"Error querying region {region_name}: {e}")
        return None

# Função para salvar os municípios em um arquivo GeoJSON
def save_municipios_to_geojson(municipios, region_name, folder="geojsons"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    geojson_filename = f"{folder}/{region_name}_municipios.geojson"
    municipios.to_file(geojson_filename, driver="GeoJSON")
    #print(f"\nRegion {region_name} saved to {geojson_filename}")

# Função para gerar o grafo
def generate_graph_from_municipios(municipios_combined, G_roads):
    G = nx.Graph()
    total_municipios = len(municipios_combined)

    # Adicionar nós ao grafo para cada município
    for idx, row in municipios_combined.iterrows():
        municipio_name = row["name"]
        print(f"Fase1: {idx + 1}/{total_municipios}")

        if municipio_name not in G:  # Garantir que o nó não foi adicionado ainda
            G.add_node(municipio_name, geometry=row["geometry"])
        # Calcular o centroide do município e o nó mais próximo da rede viária
        centroid = row["geometry"].centroid
        nearest_node = ox.distance.nearest_nodes(G_roads, centroid.x, centroid.y)
        G.nodes[row["name"]]['nearest_node'] = nearest_node

    # Identificar os vizinhos usando interseções de fronteiras
    for i, row_i in municipios_combined.iterrows():
        print(f"Fase2: {i + 1}/{total_municipios}")
        for j, row_j in municipios_combined.iterrows():
            if i != j:  # Evitar comparar o município consigo mesmo
                if row_i["geometry"].touches(row_j["geometry"]):  # Se os municípios são vizinhos
                    node_i = G.nodes[row_i["name"]]['nearest_node']
                    node_j = G.nodes[row_j["name"]]['nearest_node']

                    # Verificar se os nós estão conectados
                    if nx.has_path(G_roads, node_i, node_j):
                        # Calcular a distância entre os nós usando a rede viária
                        distance = nx.shortest_path_length(G_roads, node_i, node_j, weight='length') / 1000  # em km
                        G.add_edge(row_i["name"], row_j["name"], weight=distance)
                    else:
                        continue
                        #print(f"No path between {row_i['name']} and {row_j['name']}")

    return G

# Função para salvar o dicionário de distâncias
def save_distance_dict(G, filename="distances_dict.py"):
    distances_dict = {}
    for u, v, data in G.edges(data=True):
        distance = round(data['weight'], 3)  # Round the distance to 3 decimal places
        if u not in distances_dict:
            distances_dict[u] = []
        distances_dict[u].append((v, distance))

    with open(filename, "w") as file:
        file.write("distances_dict = {\n")
        for city, distances in distances_dict.items():
            file.write(f"    '{city}': {distances},\n")
        file.write("}\n")

    print(f"Distance dictionary saved to {filename}")

# Função para visualizar e salvar a imagem do grafo com disposição geográfica
def plot_and_save_graph(G, labeled_filename="grafo_municipios_labeled.png", dots_filename="grafo_municipios_dots.png"):
    # Increase figure size for visibility
    figsize = max(20, len(G.nodes) // 50)  # Scale based on node count
    plt.figure(figsize=(figsize, figsize))

    # Extract node positions
    pos = {node: (G.nodes[node]['geometry'].centroid.x, G.nodes[node]['geometry'].centroid.y) for node in G.nodes}

    # First plot: Labels and distances
    plt.figure(figsize=(figsize, figsize))
    nx.draw(G, pos, with_labels=True, node_size=40, font_size=8, node_color='skyblue', font_color='black')
    edge_labels = {(u, v): f"{data['weight']:.3f} km" for u, v, data in G.edges(data=True) if data['weight'] > 100}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    plt.title("Grafo de Municípios de Portugal")
    plt.savefig(labeled_filename, dpi=600)
    plt.show()
    print(f"Graph with labels saved to {labeled_filename}")

    # Second plot: Blue dots only
    plt.figure(figsize=(figsize, figsize))
    nx.draw(G, pos, with_labels=False, node_size=10, node_color='blue')
    plt.title("Nodes Only - Grafo de Municípios")
    plt.savefig(dots_filename, dpi=600)
    plt.show()
    print(f"Graph with dots only saved to {dots_filename}")





def main():
    # Definir as regiões a serem consultadas
    regions = [
        "Aveiro", "Beja", "Braga", "Bragança", "Castelo Branco", "Coimbra", "Évora", "Faro", "Guarda",
        "Leiria", "Lisboa", "Portalegre", "Porto", "Santarém", "Setúbal", "Viana do Castelo",
        "Vila Real", "Viseu"
    ]

    # Definir a rede viária para o país inteiro
    place_name = "Portugal"
    G_roads = ox.graph_from_place(place_name, network_type='drive',
                                    custom_filter='["highway"~"motorway|trunk|primary"]')
                                    #custom_filter = '["Main road"]')

    # Criar uma lista pa1ra armazenar os dados dos municípios
    municipios_list = []

    #Testar a usar portugal
    municipios_combined = get_municipios_from_region(place_name)

    # Assuming the column containing the names of the municipalities is called 'name'
    if 'name' in municipios_combined.columns:
        for name in municipios_combined['name']:
            print(name)
    else:
        print("The GeoDataFrame does not contain a 'name' column.")

    #Loop para obter os municípios de cada região com barra de progresso
    #for region in tqdm(regions, desc="Consultando a região...", unit="região"):
        # Update the description dynamically for each region
    #    tqdm.write(f"\nConsultando a região {region}...")  # Print region name in the console

    #   municipios = get_municipios_from_region(region)
    #    if municipios is not None:
            # Filtrar para adicionar apenas os municípios do continente
            # municipios = municipios[municipios['name'].isin(municipios_continentais)]
            #if not municipios.empty:
    #        save_municipios_to_geojson(municipios, region)
    #        municipios_list.append(municipios)

    # Combinar todos os municípios em um único GeoDataFrame
    #print(f"A criar o mapa completo...")
    #municipios_combined = gpd.GeoDataFrame(pd.concat(municipios_list, ignore_index=True))

    # Gerar o grafo
    print(f"A criar o grafo completo...")
    G = generate_graph_from_municipios(municipios_combined, G_roads)

    # Salvar o dicionário de distâncias
    print(f"A salvar o dicionário com as distâncias e nomes...")
    save_distance_dict(G)

    # Salvar a imagem do grafo com disposição geográfica
    print(f"A guardar a imagem...")
    plot_and_save_graph(G)


if __name__ == "__main__":
    main()

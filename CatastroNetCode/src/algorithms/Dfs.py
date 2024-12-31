from src.Graph import Graph

def procuraDFS(graph, vehicles, start, end, path=[], visited=set()):
    peopleInNeed = graph.getCity(end).population

    path.append(start)
    visited.add(start)

    if start == end:
        # calcular o custo do caminho funçao calcula custo.
        custoT = graph.pathCost(path, vehicles, peopleInNeed)
        return path, custoT
    for (neighbour, road) in graph.getNeighborsRoadPair(start):
        if neighbour not in visited:
            resultado = procuraDFS(graph, vehicles, neighbour, end, path, visited)
            if resultado is not None:
                return resultado
    path.pop()
    return None
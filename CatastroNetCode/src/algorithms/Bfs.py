#####################################################
# Procura BFS
######################################################

def procura_BFS(self, start, end):
    # definir nodos visitados para evitar ciclos
    visited = set()
    fila = Queue()
    custo = 0
    # adicionar o nodo inicial à fila e aos visitados
    fila.put(start)
    visited.add(start)

    parent = dict()
    parent[start] = None

    path_found = False
    while not fila.empty() and path_found == False:
        nodo_atual = fila.get()
        if nodo_atual == end:
            path_found = True
        else:
            for (adjacente, peso) in self.m_graph[nodo_atual]:
                if adjacente not in visited:
                    fila.put(adjacente)
                    parent[adjacente] = nodo_atual
                    visited.add(adjacente)

    # reconstruir o caminho

    path = []
    if path_found:
        path.append(end)
        while parent[end] is not None:
            path.append(parent[end])
            end = parent[end]
        path.reverse()
        # funçao calcula custo caminho
        custo = self.calcula_custo(path)
    return (path, custo)
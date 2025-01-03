##########################################
#    A*
##########################################

from City import City

def getH(graph, node, target):
    # nCity = graph.getCity(node)

    # tTargets = map(lambda t: nCity.distance_to(graph.getCity(t)), targets)
    # tsTargets = sorted(tTargets)
    # return tsTargets.pop()

    nCity = graph.getCity(node)
    if (nCity == None): return 0x7fffffff
    return nCity.distance_to(graph.getCity(target))

def aStarSearch(graph, vehicles, start, end):
    print(graph, vehicles, start, end)

    # open_list é uma lista de nós que foram visitados, mas cujos vizinhos não foram inspeccionados, começa com o nó inicial
    # closed_list é uma lista de nós que foram visitados e cujos os vizinhos foram inspeccionados
    open_list = {start}
    closed_list = set([])

    # g contém as distâncias atuais de start_node para todos os outros nós
    g = {}

    g[start] = 0

    # parents contém um mapa de adjacência de todos os nós
    parents = {}
    parents[start] = start
    reconst_path = []
    
    ret = {}
    for v in vehicles:
        ret[v.name] = {}

    for t in end:
        # costs[t] = 0
        for v in vehicles:
            ret[v.name][t] = [0, []]

        while len(open_list) > 0:
            n = None

            # print("OL:", open_list)

            # encontrar um nó com o valor mais baixo de f() - função de avaliação
            for v in open_list:
                # if n == None or g[v] + self.getH(v) < g[n] + self.getH(n):
                # print("Candidate:", v, getH(graph, v, t))
                # print("Current:", n, getH(graph, n, t))
                if n == None or g[v] + getH(graph, v, t) < g[n] + getH(graph, n, t):
                    # print("Candidate better.")
                    n = v

            # print("Evaluating:", n)

            if n == None:
                print('Path does not exist2!')
                return None

            # se o nó atual for o stop_node, então começamos a reconstruir o caminho do mesmo até ao start_node
            if n == t:
                while parents[n] != n:
                    # costs[t] = costs[t] + graph.getRoadCost(vehicles[0], n, parents[n])
                    for v in vehicles:
                        ret[v.name][t][0] += graph.getRoadCost(v, n, parents[n])
                        ret[v.name][t][1].append(n)

                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start)

                reconst_path.reverse()
                for v in vehicles:
                    ret[v.name][t][1].reverse()

                # print("AS REC:", reconst_path)
                # return (reconst_path, 0)
                break

            # para todos os vizinhos do nó atual
            for (m, road) in graph.getNeighborsRoadPair(n):
                # print("Evaluating neighbor:", m, road)

                # se o nó atual não estiver em open_list e closed_list, adicione-se a open_list
                if m not in open_list and m not in closed_list:
                    # print("Unevaluated. Adding to open list.")
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + road.distance

                else:
                    # print("Evaluated.")
                    if g[m] > g[n] + road.distance:
                        # print("Better path found. Updating.")
                        g[m] = g[n] + road.distance
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remova n da open_list e adicione-o close_list porque todos os seus vizinhos foram inspecionados
            open_list.remove(n)
            closed_list.add(n)

    # print('Path does not exist!')
    # return None

    # return (reconst_path, costs)
    return (reconst_path, ret)
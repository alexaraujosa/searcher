##########################################
#    A*
##########################################

def procura_aStar(self, start, end):
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

    while len(open_list) > 0:
        n = None

        # encontrar um nó com o valor mais baixo de f() - função de avaliação
        for v in open_list:
            if n == None or g[v] + self.getH(v) < g[n] + self.getH(n):
                n = v
        if n == None:
            print('Path does not exist!')
            return None

        # se o nó atual for o stop_node, então começamos a reconstruir o caminho do mesmo até ao start_node
        if n == end:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]

            reconst_path.append(start)

            reconst_path.reverse()

            return (reconst_path, self.calcula_custo(reconst_path))

        # para todos os vizinhos do nó atual
        for (m, weight) in self.getNeighbours(n):
            # se o nó atual não estiver em open_list e closed_list, adicione-se a open_list
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight

            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)

        # remova n da open_list e adicione-o close_list porque todos os seus vizinhos foram inspecionados
        open_list.remove(n)
        closed_list.add(n)

    print('Path does not exist!')
    return None
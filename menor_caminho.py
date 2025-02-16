my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C',1 ), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

def menor_caminho(graph, start, target = ''):
    unvisited = list(graph)
    distancias = {node: 0 if node == start else float('inf') for node in graph}
    caminhos = {node: [] for node in graph}
    caminhos[start].append(start)
    
    while unvisited:
        atual = min(unvisited, key=distancias.get)
        for node, distance in graph[atual]:
            if distance + distancias[atual] < distancias[node]:
                distancias[node] = distance + distancias[atual]
                if caminhos[node] and caminhos[node][-1] == node:
                    caminhos[node] = caminhos[atual][:]
                else:
                    caminhos[node].extend(caminhos[atual])
                caminhos[node].append(node)
        unvisited.remove(atual)
    
    printar = [target] if target else graph
    for node in printar:
        if node == start:
            continue
        print(f'\n{start}-{node} distancia: {distancias[node]}\nCaminho: {" -> ".join(caminhos[node])}')
    
    return distancias, caminhos
    
menor_caminho(my_graph, 'A', 'D')
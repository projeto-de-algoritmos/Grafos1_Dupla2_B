import collections

def main(graph, root): 
    #{0: ['1', '2'], 1: [], 2: []}
    visitado, lista = set(), collections.deque([root])

    fofocado = []
    fofocado.append(root)
    while lista: 
        print(lista)
        vertex = lista.popleft()

        for vizinho in graph[vertex]: 
            if vizinho not in visitado:
                fofocado.append(vizinho)
                visitado.add(vizinho)
                lista.append(vizinho)
    return fofocado

    
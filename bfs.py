import collections
import grafo

def main(graph, root): 

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

    
def investigarcidade(h, fofocado):
    graph = grafo.Graph(h)
    nos = graph.vertices()
    tamanhografo = nos.__len__()
    tamanhofofocado = fofocado.__len__()

    if tamanhografo == tamanhofofocado:
        print('A cidade inteira já sabe da fofoca')
    else:
        print('nem todos da cidade sabem da fofoca')

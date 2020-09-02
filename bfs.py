import collections

def main(graph, root): 
    visitado, lista = set(), collections.deque([root])
    fofocado = []
    while lista: 
        print(lista)
        vertex = lista.popleft()
        
        for vizinho in graph[vertex]: 
            if vizinho not in visitado:
                fofocado.append(vizinho)
                visitado.add(vizinho) 
                lista.append(vizinho)
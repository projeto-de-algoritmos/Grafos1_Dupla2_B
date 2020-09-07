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
                r = encontrar(vizinho, fofocado)
                if r :
                    fofocado.append(vizinho)
                else :
                    print('entrou')    
                visitado.add(vizinho)
                lista.append(vizinho)
    return fofocado

    
def investigarcidade(h, fofocado):
    print(fofocado)
    graph = grafo.Graph(h)
    nos = graph.vertices()
    tamanhografo = nos.__len__()
    tamanhofofocado = fofocado.__len__()

    if tamanhofofocado == tamanhografo:
        print('A cidade inteira já sabe da fofoca')
        print('esses são os que sabem da fofoca:')
        print (fofocado)
    else:
        print('nem todos da cidade sabem da fofoca')
        print('esses são os que sabem da fofoca:')
        print (fofocado)

def encontrar(elemento, lista):
    for i in range (len(lista)):
            if elemento in lista[i]:
                return False
            else: 
                return True
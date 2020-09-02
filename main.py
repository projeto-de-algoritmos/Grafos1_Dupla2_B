import grafo
import bfs
import pickle

h = {}
numnos = int(input('digite o numero de nós:\n'))

for i in range(0,numnos):
  vizinho = list(input('indique os vizinhos de ' + str(i) + ':'))
  print(vizinho)
  h[i] = vizinho

print(h)
# h = {0:[1, 2], 1:[3,4],2:[5],3:[],4:[],5:[]}
 
graph = grafo.Graph(h)

print("vertices:")
print(graph.vertices())

print("arestas:")
print(graph.edges())

print("Fazer busca em largura")
bfs.main(h, 0)

##print("Add vertex:")
##graph.add_vertex("z")

##print("Vertices of graph:")
##print(graph.vertices())

##print("Add an edge:")
##graph.add_edge({"a","z"})

##print("Vertices of graph:")
##print(graph.vertices())

##print("Edges of graph:")
##print(graph.edges())

# print('Adding an edge {"x","y"} with new vertices:')
# graph.add_edge({"x","y"})
# print("Vertices of graph:")
# print(graph.vertices())
# print("Edges of graph:")
# print(graph.edges())




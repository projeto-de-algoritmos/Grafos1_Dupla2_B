import grafo
import bfs
import pickle

h = {}
numnos = int(input('digite o numero de nós:\n'))

for i in range(0,numnos):
  nomeno = input('digite o nome ou numero de nó ' + str(i) + ' : ')
  vizinho = list(input('indique os vizinhos de ' + str(nomeno) + ' : '))
  print(vizinho)
  h[str(nomeno)] = vizinho

print(h)

#teste = {0:[1, 2], 1:[3,4],2:[5],3:[],4:[],5:[]}
 
graph = grafo.Graph(h)

print("esses sao os vertices do grafo:")
print(graph.vertices())

print("essas sao as arestas do grafo:")
print(graph.edges())

print("Fazer busca em largura")
nobfs = input('digite o nó que quer que comece a busca:\n')
bfs.main(h, nobfs)

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




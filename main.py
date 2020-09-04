import grafo
import bfs

h = {}
vizinhos = []
numnos = int(input('digite o numero de nós:\n'))

for i in range(0,numnos):

  nomeno = input('digite o nome ou numero de nó ' + str(i) + ' : ')
  numvizinhos = int(input('digite o numero de vizinhos do'+ str(nomeno) + ':' ))

  for j in range(0,numvizinhos):
    vizinho = input('indique o ' + str(j+1) + 'vizinho:')
    vizinhos.append(vizinho)
    
  h[str(nomeno)] = vizinhos

  print(h)
#teste = {0:[1, 2], 1:[3,4],2:[5],3:[],4:[],5:[]}
 
graph = grafo.Graph(h)

print("esses sao os vertices do grafo:")
print(graph.vertices())
vertices = graph.vertices()

print("essas sao as arestas do grafo:")
print(graph.edges())

print("Fazer busca em largura")
nobfs = input('digite o nó que quer que comece a busca:\n')
fofocado = bfs.main(h, nobfs)

if(fofocado == vertices):
  print('toda a cidade sabe da fofoca')
else:
  print('nem todos da cidade sabem da fofoca')

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
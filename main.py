import grafo
import bfs

h = { 0 : [1, 2],  ,
      1 : [],
      2 : [],  
    }

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




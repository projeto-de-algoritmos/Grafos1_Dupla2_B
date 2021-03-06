import grafo
import bfs
import criagrafo
import gerador_aleatorio


#teste = {0:[1, 2], 1:[3,4],2:[5],3:[],4:[],5:[]}

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Criar grafo de cidade inserindo os nós manualmente")
    print("2. Criar grafo de cidade aleatoriamente")
    print("3. Mostrar informações do grafo") 
    print("4. Espalhar fofoca pela cidade")
    print("5. Investigar se toda cidade sabe da fofoca")
    print("6. Sair")
    print(67 * "-")
  


if __name__ == '__main__':
    loop=True
    
    while loop:
        print_menu()
        choice = input("Entre sua opcao [1-5]: ")
        if choice=='1':     
            print("Opcao 1 foi escolhida")
            h = criagrafo.main()
        elif choice=='2':
            print("Opcao 2 foi escolhida")
            print("voce deve digitar o numero de pessoas da cidade: (obs: numero recomendado no maximo 30000)\n")
            numnos = int(input('Digite o numero de pessoas:'))
            nummaxvizinhos = int(input('Digite o numero maximo de conhecidos de cada pessoa:'))
            h = gerador_aleatorio.main(numnos, nummaxvizinhos)            
        elif choice=='3':
            print("Opcao 3 foi escolhida")
            graph = grafo.Graph(h)
            print("este é seu grafo:")
            print(h)
            print("esses sao os vertices do grafo:")
            print(graph.vertices())
            vertices = graph.vertices()
            print("essas sao as arestas do grafo:")
            print(graph.edges())
        elif choice=='4':
            print("Opcao 4 foi escolhida")
            print("Mauricio disse que js é melhor python")
            print("Espalhar fofoca pela cidade usando busca em largura")
            nobfs = input('digite o nó que será o primeiro fofoqueiro:\n')
            fofocado = bfs.main(h, nobfs)
        elif choice=='5':
            print("Opcao 5 foi escolhida")
            bfs.investigarcidade(h, fofocado)
        elif choice=='6':
            print("Opcao 6 foi escolhida")
            print('Saindo....')
            loop=False

        else:
            input("Opcao incorreta. Aperte qualquer tecla para tentar novamente..")

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
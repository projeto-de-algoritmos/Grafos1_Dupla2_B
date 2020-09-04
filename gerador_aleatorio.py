import random

def geradorNumeroAleatorio(maximo) :
    lis = []
    while len(lis) < maximo:
        #This checks to see if there are duplicate numbers
        r = random.randint(1,maximo)
        if r not in lis :
            lis.append(r)
    return lis

def geradorgrafoaleatorio(nos):

    lista_nos = geradorNumeroAleatorio(nos)
    grafo = {}
    lista_vizinhos = []
    for i in lista_nos:
        num_vizinhos = random.randint(1,2)
        lista_vizinhos = geradorNumeroAleatorio(num_vizinhos) 
        grafo[str(i)] = lista_vizinhos
    return grafo

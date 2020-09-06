import random

def geradorNumeroAleatorio(maximo) :
    lis = []
    while len(lis) < maximo:
        r = random.randint(1,maximo)
        if str(r) not in lis :
            lis.append(str(r))
    return lis

def main(nos,nummaxvizinhos):

    lista_nos = geradorNumeroAleatorio(nos)
    grafo = {}
    lista_vizinhos = []
    for i in lista_nos:
        num_vizinhos = random.randint(1,nummaxvizinhos)
        lista_vizinhos = geradorNumeroAleatorio(num_vizinhos) 
        grafo[str(i)] = lista_vizinhos
    return grafo

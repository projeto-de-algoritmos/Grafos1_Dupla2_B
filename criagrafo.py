
def main():
    h = {}
    
    numnos = int(input('digite o numero de pessoas:\n'))

    for i in range(0,numnos):
        vizinhos = []
        nomeno = input('represente a pessoa por um nome ou numero ' + str(i) + ' :')
        numvizinhos = int(input('digite o numero de conhecidos do ' + str(nomeno) + ' :' ))

        for j in range(0,numvizinhos):
            vizinho = input('indique o ' + str(j+1) + ' conhecido:')
            vizinhos.append(vizinho)    
        h[str(nomeno)] = vizinhos
    return h 

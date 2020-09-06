
def main():
    h = {}
    vizinhos = []
    numnos = int(input('digite o numero de pessoas:\n'))

    for i in range(0,numnos):

        nomeno = input('represente a pessoa por um nome ou numero ' + str(i) + ' :')
        numvizinhos = int(input('digite o numero de vizinhos do ' + str(nomeno) + ' :' ))

        for j in range(0,numvizinhos):
            vizinho = input('indique o ' + str(j+1) + ' vizinho:')
            vizinhos.append(vizinho)
            
        h[str(nomeno)] = vizinhos
    return h 

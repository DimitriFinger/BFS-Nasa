class Nodo:  
        self.data = data
        self.vizinhos = []
        self.x = x
        self.y = y


class Grafo:
    def __init__(self):
        self.listaAdjacencia = []

    def addNodo(self, nodo):
        if isinstance(nodo, Nodo) and nodo.data not in self.listaAdjacencia:
            self.listaAdjacencia.append(nodo)
            return True
        else:
            return False
 
#imprime cada nodo, sua posição e seus nodos adjacentes
    def imprimeLista(self):
        for n in range(len(self.listaAdjacencia)):
            print(str(self.listaAdjacencia[n].data) +"  "+ str(self.listaAdjacencia[n].x+1)  +"  "+ str(self.listaAdjacencia[n].y+1) )

            for i in range(len(self.listaAdjacencia[n].vizinhos)):
                vizinho = self.listaAdjacencia[n].vizinhos
                print("vizinhos " + str(vizinho[i].data + " " +str(vizinho[i].x + 1) + " "+str(vizinho[i].y+1)))


#retorna numero de vertices possíveis da entrada
def contaVertices(matriz):
    vertices = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == '.' or matriz[i][j].isalpha():
                vertices += 1
    return vertices


#cria grafo / cria nodos do grafo, sua lista de adjacencia e adiciona arestas entre os porais
def criaGrafo(matriz):
    graph = Grafo()
   
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == '.' or matriz[i][j].isalpha():
                node = Nodo(matriz[i][j], i, j)
                graph.addNodo(node)
                if i<len(matriz)-1:
                    if matriz[i+1][j] == '.' or matriz[i+1][j].isalpha():
                            node2 = Nodo(matriz[i+1][j], i+1, j)
                            node.vizinhos.append(node2)                            
                            #print("nodo inferior adicionado!")

                if j<len(matriz[0])-1:
                    if matriz[i][j+1] == '.' or matriz[i][j+1].isalpha():
                            node2 = Nodo(matriz[i][j+1], i, j+1)                    
                            node.vizinhos.append(node2)
                            #print("nodo lateral direito adicionado!")

                if i>0:
                    if matriz[i-1][j] == '.' or matriz[i-1][j].isalpha():
                            node2 = Nodo(matriz[i-1][j], i-1, j)
                            node.vizinhos.append(node2)
                            #print("nodo superior adicionado!")
                
                if j>0:
                    if matriz[i][j-1] == '.' or matriz[i][j-1].isalpha():
                            node2 = Nodo(matriz[i][j-1], i, j-1)
                            node.vizinhos.append(node2)
                            #print("nodo lateral esquerdo adicionado!")


# cria arestas entre os portais
    for n in range(len(graph.listaAdjacencia)):
        if graph.listaAdjacencia[n].data.isalpha():
            for m in range(len(graph.listaAdjacencia)):
                if graph.listaAdjacencia[m].data == graph.listaAdjacencia[n].data and m != n:
                      graph.listaAdjacencia[m].vizinhos.append(graph.listaAdjacencia[n])  
                            
                      
    return graph

if __name__ == "__main__":

    arq = open('teste.txt', 'r')
    texto = []
    matriz = []
    texto = arq.readlines()
    #imprime arquivo
    for i in range(len(texto)):
        matriz.append(texto[i].replace('\n', ''))
    for i in range(len(texto)):
        print(matriz[i])
    
    #print(contaVertices(matriz)) 
    arq.close()

    graph = criaGrafo(matriz)

    graph.imprimeLista()







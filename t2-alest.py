class Nodo:  
    def __init__(self, data, x, y):
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

    #retorna número de vertices na lista de vertices
    def retornaVertices(self):
        return len(self.listaAdjacencia)
 
    #imprime cada nodo, sua posição e seus nodos adjacentes
    def imprimeLista(self):
        for n in range(len(self.listaAdjacencia)):
            print(str(self.listaAdjacencia[n].data) +"  "+ str(self.listaAdjacencia[n].x+1)  +"  "+ str(self.listaAdjacencia[n].y+1) )

            for i in range(len(self.listaAdjacencia[n].vizinhos)):
                vizinho = self.listaAdjacencia[n].vizinhos
                print("vizinhos " + str(vizinho[i].data + " " +str(vizinho[i].x + 1) + " "+str(vizinho[i].y+1)))


class Caminhamento:
    def __init__(self, G, maxX, maxY):        
        #self.start = start # A
        self.G = G
        self.maxX = maxX - 1
        self.maxY = maxY - 1

    def bfs(self):
        marked = [False] * self.G.retornaVertices()
        edgeTo = [None] * self.G.retornaVertices()
        distTo = [None] * self.G.retornaVertices()
        fila = []

        for n in range(len(self.G.listaAdjacencia)):
                if self.G.listaAdjacencia[n].data == 'A':                    
                    if self.G.listaAdjacencia[n].x == 0 or self.G.listaAdjacencia[n].y == 0:    
                        print("achei o A externo")
                        print(str(self.G.listaAdjacencia[n].data + " " +str(self.G.listaAdjacencia[n].x + 1) + " "+str(self.G.listaAdjacencia[n].y+1)))
                        fila.append(n)
                        marked[n] = True   
                    if self.G.listaAdjacencia[n].x == self.maxX or self.G.listaAdjacencia[n].y == self.maxY:
                        print("achei o A externo")
                        print(str(self.G.listaAdjacencia[n].data + " " +str(self.G.listaAdjacencia[n].x + 1) + " "+str(self.G.listaAdjacencia[n].y+1)))
                        marked[n] = True
                        fila.append(n)    
        print(len(fila))
        while len(fila) != 0:            
            print("entrou no while")
            v = fila.pop(0)
            print(len(fila))
            #print(marked[0])
            for w in range(len(self.G.listaAdjacencia[v].vizinhos)):
                print(str(self.G.listaAdjacencia[v].vizinhos[w].data) + ' ' +str(self.G.listaAdjacencia[v].vizinhos[w].x+1) + ' ' + str(self.G.listaAdjacencia[v].vizinhos[w].y+1) )
                #print(marked[w])                
                for x in range(len(self.G.listaAdjacencia)):
                    if self.G.listaAdjacencia[x].x == self.G.listaAdjacencia[v].vizinhos[w].x:
                         if self.G.listaAdjacencia[x].y == self.G.listaAdjacencia[v].vizinhos[w].y: 
                            if not marked[x]:
                                print("marcou")
                                marked[x] = True
                                fila.append(x)
        print("saiu")


#cria grafo / cria nodos do grafo, sua lista de adjacencia e adiciona arestas entre os portais
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

    # adiciona adjacencias entre os portais
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
    
    #print(retornaVertices())  # Número de possiveis vertices na matriz fornecida
    arq.close()
    graph = criaGrafo(matriz)

    maxX = len(matriz)
    maxY = len(matriz[0])
    #print(len(matriz))
    #print(len(matriz[0]))
    #v = print(graph.retornaVertices())
    
    bfs = Caminhamento(graph, maxX, maxY)
    bfs.bfs()
    
    #graph.imprimeLista()







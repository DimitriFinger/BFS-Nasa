class Nodo:  
    def __init__(self, data, x, y):
        self.data = data
        self.vizinhos = []
        self.x = x
        self.y = y
        self.nodoPai = -1 

class Grafo:
    def __init__(self):
        self.listaAdjacencia = []

    def adicionaNodo(self, nodo):
        if isinstance(nodo, Nodo) and nodo.data not in self.listaAdjacencia:
            self.listaAdjacencia.append(nodo)
            return True
        else:
            return False

    #retorna número de vertices na lista de vertices
    def retornaVertices(self):
        return len(self.listaAdjacencia)
 
    #imprime cada nodo, sua posição e seus nodos adjacentes
    def imprimeAdjacentes(self):
        for n in range(len(self.listaAdjacencia)):
            print(str(self.listaAdjacencia[n].data) +"  "+ str(self.listaAdjacencia[n].x+1)  +"  "+ str(self.listaAdjacencia[n].y+1) )

            for i in range(len(self.listaAdjacencia[n].vizinhos)):
                vizinho = self.listaAdjacencia[n].vizinhos
                print("vizinhos " + str(vizinho[i].data + " " +str(vizinho[i].x + 1) + " "+str(vizinho[i].y+1)))

# Classe responsável por realizar a busca bfs pelo grafo
class Caminhamento:
    def __init__(self, G, maxX, maxY, comeco, fim):        
        #self.start = start # A
        self.G = G
        self.maxX = maxX - 1
        self.maxY = maxY - 1
        self.comeco = comeco
        self.fim = fim

    def bfs(self):
        marked = [False] * self.G.retornaVertices()
        fila = []

        # Procura localização do vertice para começar
        for n in range(len(self.G.listaAdjacencia)):
                if self.G.listaAdjacencia[n].data == self.comeco:                    
                    if self.G.listaAdjacencia[n].x == 0 or self.G.listaAdjacencia[n].y == 0:    
                        print("A em " + str(self.G.listaAdjacencia[n].x+1) +' '+ str(self.G.listaAdjacencia[n].y+1))
                        fila.append(n)
                        marked[n] = True 
                        entrada = n
                        break
                          
                    if self.G.listaAdjacencia[n].x == self.maxX or self.G.listaAdjacencia[n].y == self.maxY:
                        print("A em " + str(self.G.listaAdjacencia[n].x+1) +' '+ str(self.G.listaAdjacencia[n].y+1))                        
                        marked[n] = True
                        fila.append(n)
                        entrada = n
                        break
                         

        # Procura localização vertice final
        for n in range(len(self.G.listaAdjacencia)):
                if self.G.listaAdjacencia[n].data == self.fim:                    
                    if self.G.listaAdjacencia[n].x != 0 and self.G.listaAdjacencia[n].y != 0:
                        if self.G.listaAdjacencia[n].x < self.maxX and self.G.listaAdjacencia[n].y < self.maxY:    
                            print("Z em " + str(self.G.listaAdjacencia[n].x+1) +' '+ str(self.G.listaAdjacencia[n].y+1) ) 
                            saida = n
                            

        # Realiza a busca marcando nodos e identificando nodos nodoPai
        while len(fila) != 0:
            v = fila.pop(0)            
            for w in range(len(self.G.listaAdjacencia[v].vizinhos)):                            
                for x in range(len(self.G.listaAdjacencia)):
                    if self.G.listaAdjacencia[x].x == self.G.listaAdjacencia[v].vizinhos[w].x:
                         if self.G.listaAdjacencia[x].y == self.G.listaAdjacencia[v].vizinhos[w].y: 
                            if not marked[x]:
                                marked[x] = True
                                self.G.listaAdjacencia[x].nodoPai = v
                                fila.append(x)
            if self.G.listaAdjacencia[v] == self.G.listaAdjacencia[saida]:
                #print("achei z")
                break       
       
        # Armazena caminho percorrido 
        contaSaltos = 0
        atual = saida
        vetorCaminho = []
        vetorCaminho.append(atual)
        while True:
            if self.G.listaAdjacencia[atual].nodoPai > 1:
               atual = self.G.listaAdjacencia[atual].nodoPai
               vetorCaminho.append(atual)
               contaSaltos+=1
            elif self.G.listaAdjacencia[atual] == self.G.listaAdjacencia[entrada]:
               break

        # Imprime caminho percorrido 
        vetorCaminho.reverse()                
        for w in range(len(vetorCaminho)):
            #print(vetorCaminho[w])
            contaSaltos=w
            print(str(self.G.listaAdjacencia[vetorCaminho[w]].data) + ' ' +str(self.G.listaAdjacencia[vetorCaminho[w]].x+1) + ' ' + str(self.G.listaAdjacencia[vetorCaminho[w]].y+1) + ' ( ' +str(contaSaltos) +' )' )


#cria grafo / cria nodos do grafo, sua lista de adjacencia e adiciona arestas entre os portais
def criaGrafo(matriz):
    grafo = Grafo()
   
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == '.' or matriz[i][j].isalpha():
                node = Nodo(matriz[i][j], i, j)
                grafo.adicionaNodo(node)
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
    for n in range(len(grafo.listaAdjacencia)):
        if grafo.listaAdjacencia[n].data.isalpha():
            for m in range(len(grafo.listaAdjacencia)):
                if grafo.listaAdjacencia[m].data == grafo.listaAdjacencia[n].data and m != n:
                      grafo.listaAdjacencia[m].vizinhos.append(grafo.listaAdjacencia[n])                 
    return grafo


if __name__ == "__main__":

    #Tratamento do arquivo de entrada
    arq = open('caso1.txt', 'r') # Escolher qual arquivo deseja usar
    texto = []
    matriz = []
    linhas = arq.readlines()
    texto = linhas[1:]
    entrada = linhas[0].split(" ")
    comeco = entrada[0]
    fim = entrada[1].replace('\n', '')

    #imprime matriz
    for i in range(len(texto)):
        matriz.append(texto[i].replace('\n', ''))
    for i in range(len(texto)):
        print(matriz[i])
    
    #print(retornaVertices())  # Número de possiveis vertices na matriz fornecida    
    grafo = criaGrafo(matriz)

    maxX = len(matriz)
    maxY = len(matriz[0])
    
    bfs = Caminhamento(grafo, maxX, maxY, comeco, fim)
    bfs.bfs()
    
    #grafo.imprimeAdjacentes() #Remover comentário para retornar lista de adjacentes de cada vértice







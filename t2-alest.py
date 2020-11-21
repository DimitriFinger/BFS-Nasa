arq = open('teste.txt', 'r') 
texto = []  
matriz = [] 
texto = arq.readlines()

for i in range(len(texto)):          
    matriz.append(texto[i].replace('\n',''))  

for i in range(len(texto)):        
    print(matriz[i])  

print(matriz[0][0])
arq.close() 
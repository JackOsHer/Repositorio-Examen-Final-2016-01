#Dada el siguiente arreglo "n" de 2 dimensiones:n =[[1, 11, -5, 3],[3, 22, -2, 4],[5, 10, -6, 8],[9, 16, -1, 3]]
#Calcule programáticamente (usando iteraciones) el número de mayor valor ubicado en la diagonal principal.


n = [[1, 11, -5, 3],[3, 22, -2, 4],[5, 10, -6, 8],[9, 16, -1, 3]]
diagonal = []

for i in range(len(n)):
    diagonal.append(n[i][i])
    
mayor=diagonal[0]
if diagonal[1]>diagonal[0] and diagonal[1]>diagonal[2] and diagonal[1]>diagonal[3]:
    mayor = diagonal[1]
if diagonal[2]>diagonal[0] and diagonal[2]>diagonal[1] and diagonal[2]>diagonal[3]:
    mayor = diagonal[2]
if diagonal[3]>diagonal[0] and diagonal[3]>diagonal[1] and diagonal[3]>diagonal[2]:
    mayor = diagonal[3]

print(mayor)

        



filas = 3
columnas = 4

matriz = []
numero = 1
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(numero)
        numero += 1
    matriz.append(fila)

for fila in matriz:
    for elemento in fila:
        print(elemento, end="\t")
    print()  

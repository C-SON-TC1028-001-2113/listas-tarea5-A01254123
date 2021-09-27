def menores(matriz):
    menores=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]<10:
                menores.append(matriz[i][j])
    return menores

def datos():
    elementosMatriz=[]
    filas=int(input())
    columnas=int(input())
    for i in range(filas):
        elementosMatriz.append([])
        for j in range(columnas):
            datosMatriz=int(input())
            elementosMatriz[i].append(datosMatriz)
    return menores(elementosMatriz)

def main():
    print(datos())

if __name__=='__main__':
    main()

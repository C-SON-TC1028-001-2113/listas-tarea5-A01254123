def main():
    #escribe tu código abajo de esta línea
    n=int(input())
    lista=[]
    i=0
    if n>0:
        while i<n:
            elemento=input()
            lista.append(elemento)
            i=i+1
        print(lista)
        sinDuplicar=[]
        for i in lista:
            if i not in sinDuplicar:
                sinDuplicar.append(i)
        print(sinDuplicar)   
    else:
        print("Error")
if __name__=='__main__':
    main()
    
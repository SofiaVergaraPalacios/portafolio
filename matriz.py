def abrirArchivo(archivo):
    datos= []
    ar = open(archivo, "r",encoding= "utf-8")   
    datos= ar.read().strip().split()
    A= [datos[1],datos[2]]
    B= [datos[4], datos[5]]
    return A, B
def sumar(A,B):
   i = int(A[0]) +int(B[0])
   l= int(A[1]) + int(B[1])
   c = i + l
   return c
def mostrar(c):
   print("Resultado: ", c)
def main():
   A, B = abrirArchivo("matriz.dat.txt")
   c= sumar(A,B)
   mostrar(c)
if __name__ == "__main__":
    main()
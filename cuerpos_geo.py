from math import pi, sqrt

def opciones(): #menu de opciones de cuerpos geometricos a elegir 
    print("______________________________________________________________________")
    print("\nEscriba el número de la figura geométrica que desea calcular:")
    print("______________________________________________________________________")
    print("1 - Cubo")
    print("2 - Cilindro")
    print("3 - Esfera")
    print("4 - Cono")
    print("5 - Paralelepipedo")
    print("6 - Piramide Triangular")
    print("________________________________________________________________________")
#definicion de formulas de cada cuerpo geometrico con sus variables
#cubo:
def cubo(lc):  # lc = longitud de un lado del cubo
    area_cubo = 6 * lc ** 2
    volumen_cubo = lc ** 3
    return area_cubo, volumen_cubo
#cilindro: 
def cilindro(rc, h):  # rc = radio cilindro, h = altura cilindro
    area_lateral = 2 * pi * rc * h
    area_base = pi * rc ** 2
    area_total = area_lateral + 2 * area_base
    volumen = pi * rc ** 2 * h
    return area_total, volumen
#esfera:
def esfera(rd):  # rd = radio esfera
    area_esfera = 4 * pi * rd**2
    volumen_esfera = (4/3) * pi * rd**3
    return area_esfera, volumen_esfera 
#cono:
def cono(hcn, rcn):  # hcn = altura cono, rcn = radio cono
    generatris_cono = sqrt(rcn**2 + hcn**2)
    area_cono = pi * rcn * (rcn + generatris_cono)
    volumen_cono = (1/3) * pi * rcn**2 * hcn
    return area_cono, volumen_cono
#paralelepipedo:
def paralelepipedo(a,b,c): #a=altura, b=ancho  c=largo
    area_paralelepipedo= 2*(a*b+b*c+a*c)
    volumen_paralelepipedo= a*c*b
    return area_paralelepipedo, volumen_paralelepipedo
#piramide trianular:
def piramide_triangular(ap, hp): #ap= area piramide, hp= altura piramide
    area_base_piramide= (sqrt(3)/4)*ap**2
    hp_cara= sqrt(hp**2 + (ap*sqrt(3)/6)**2)
    area_cara_piramide= (ap*hp_cara)/2
    area_t_piramide= area_base_piramide +3* area_cara_piramide  #area total
    volumen_piramide= (1/3)* area_base_piramide* hp
    return area_t_piramide, volumen_piramide
def main(): #seleccion de opciones al seleccionar un numero asociado a una opción usando if , elif , else
    while True: # usamos un while para usar el menu de manera mas eficiente
        opciones()
        print("***********************************************")
        opcion = int(input("Ingrese su opción: "))
        print("***********************************************")
        if opcion == 1:
            print("Has seleccionado Cubo.") 
            print("***********************************************")
            lc = float(input("Ingrese la longitud de un lado del cubo: "))
            area_cubo, volumen_cubo = cubo(lc)
            print("***********************************************")
            print("El área total del cubo es:", area_cubo)
            print("El volumen del cubo es:", volumen_cubo)
            print("***********************************************")
        elif opcion == 2:
            print("Has seleccionado Cilindro.")
            print("***********************************************")
            rc = float(input("Ingrese el radio del cilindro: "))
            h = float(input("Ingrese la altura del cilindro: "))
            area_total, volumen = cilindro(rc, h)
            print("***********************************************")
            print("El área total del cilindro es:", area_total)
            print("El volumen del cilindro es:", volumen)
            print("***********************************************")
        elif opcion == 3:
            print("Has seleccionado Esfera.")
            print("***********************************************")
            rd = float(input("Ingrese el radio de la esfera: "))
            area_esfera, volumen_esfera = esfera(rd)
            print("***********************************************")
            print("El área de la esfera es:", area_esfera)
            print("El volumen de la esfera es:", volumen_esfera)
            print("***********************************************")
        elif opcion == 4:
            print("Has seleccionado Cono.")
            print("***********************************************")
            hcn = float(input("Ingrese la altura del cono: "))
            rcn = float(input("Ingrese el radio del cono: "))
            area_cono, volumen_cono = cono(hcn, rcn)
            print("***********************************************")
            print("El área del cono es:", area_cono)
            print("El volumen del cono es:", volumen_cono)
            print("***********************************************")
        elif opcion== 5:
            print("Has seleccionado paralelepipedo.")
            print("***********************************************")
            a=float(input("ingrese la altura del paralelepipedo: "))
            b=float(input("ingrese el ancho del paralelepipedo: "))
            c=float(input("ingrese el largo del paralelepipedo: "))
            area_paralelepipedo, volumen_paralelepipedo=paralelepipedo(a,b,c)
            print("***********************************************")
            print("El area del paralelepipedo es: ",area_paralelepipedo)
            print("El volumen del paralelepipedo es: ", volumen_paralelepipedo)
        elif opcion==6: 
            print("Has seleccionado piramide triangular.")
            print("***********************************************")
            ap=float(input("ingrese la longitud del lado de la base de la piramide: "))
            hp=float(input("ingrese la altura de la piramide : "))
            area_t_piramide, volumen_piramide = piramide_triangular(ap,hp)
            print("***********************************************")
            print("El area total de la piramide triangular es : ", area_t_piramide)
            print("El volumen de la piramide triangular es : ", volumen_piramide)
            print("***********************************************")
        else:
            print("Error intentalo nuevamente :<!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")#integramos esta opcion si es que no se ingresa ningun n° definido en el menu 
        continuar = input("¿Desea continuar? (s/n): ").lower()
        if continuar != 's':
            print("Has salido del programa")
            break
if __name__ == "__main__":
    main()
#fin del programa
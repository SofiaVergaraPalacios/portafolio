def entrada(glucosa,edad,medicion_anos,genero):
    if medicion_anos==True:
        edad=edad/12
    if edad<=1:
        rang_min,rang_max=70,100
    elif edad>1 or edad<=5:
        rang_min,rang_max= 80,110
    elif edad>5 or edad<=12:
        rang_min,rang_max=70,130
    elif edad>12 or edad<=19:
        rang_min,rang_max= 70,120
    elif edad>19:
        if genero=="0":
            rang_min,rang_max=70,150
        elif genero=="1":
            rang_min,rang_max=70,140
        else:
         return"genero fuera de rango ingrese 1 para femenino , 0 para masculino"
    #glucosa

    if glucosa<rang_min:
        return"hipoglucemia (bajo el rango)"
    elif glucosa>rang_max:
        return "hiperglucemia (sobre el rango)"
    else:
        return "normal"

def main():
    while True:
        try:
            glucosa=float(input("ingrese su nivel de glucosa(mg/dl):"))
            edad=int(input("ingrese su edad:"))
            medicion_anos=bool(input("¿la edad sera en anos?(True=anos,False=meses)"))
            genero=input("ingrese su genero (0 para masculino, 1 para femenino):").strip()
            if genero not in ["0","1"]:
                print("genero invalido ingrese 0 para masculino, 1 para femenino: ")
            else:
                resultado=entrada(glucosa,edad,medicion_anos,genero)
            print("resultado:",resultado)
            continuar=input("¿desea continuar?(s/n)").strip().lower()
            if continuar !='s':
                    print("has salido del programa")
                    break
        except ValueError:
                print("error")
if __name__ == '__main__':
    resultado=main()
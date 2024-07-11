from math import sqrt
print("calcular ecuacion cuadratica: ")
print("................................................................")
def resolver_ecuacion(a, b, c):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return x1, x2
    else:
        return None, None

def resolver_soluciones(d):
    if d > 0:
        print("La ecuación tiene dos soluciones")
    elif d == 0:
        print("La ecuación tiene una única solución")
    else:
        print("La ecuación no tiene ninguna solución real")

def main():
    a = int(input("Ingrese el coeficiente a: "))
    b = int(input("Ingrese el coeficiente b: "))
    c = int(input("Ingrese el coeficiente c: "))
    x1, x2 = resolver_ecuacion(a, b, c)
    if x1 is not None:
        print("El valor de x1 es:", x1)
        print("El valor de x2 es:", x2)
        discriminante = b ** 2 - 4 * a * c
        resolver_soluciones(discriminante)
    else:
        print("La ecuación no tiene solución real.")

if __name__ == "__main__":
    main()

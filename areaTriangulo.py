def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo."""
    area = (base * altura) / 2
    return area

b= float(input("Ingrese la base del triángulo: "));
h = float(input("Ingrese la altura del triángulo: "))

resultado = calcular_area_triangulo(b, h)
print("El área del triángulo es:", resultado)

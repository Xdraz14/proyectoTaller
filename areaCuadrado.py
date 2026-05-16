def calcular_area_cuadrado(lado):
    area = lado ** 2
    return area

lado= float(input("Ingrese el lado del cuadrado: "));
resultado = calcular_area_cuadrado(lado )
print(f"El área del cuadrado es: {resultado}")

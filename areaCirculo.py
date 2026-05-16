import math

radio = float(input("Ingresa el valor del radio del círculo: "))

area = math.pi * (radio ** 2)

print(f"El área del círculo con radio {radio} es: {round(area, 2)}")

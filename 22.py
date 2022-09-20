import math

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

delta = b**2 - 4 * a * c

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"R1 = {raiz1:.5f}")
    print(f"R2 = {raiz2:.5f}")

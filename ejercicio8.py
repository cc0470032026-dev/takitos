##Ejercicio 8:
##Pide tres lados de un triángulo y determina si es equilátero, isósceles o escaleno.

a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a == b == c:
    print("Es un triángulo equilátero.")
elif a == b or b == c or a == c:
    print("Es un triángulo isósceles.")
else:
    print("Es un triángulo escaleno.")

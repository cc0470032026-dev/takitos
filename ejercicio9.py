##Ejercicio 9:
##Solicita un año y determina si es bisiesto.

year = int(input("Ingresa un año el que usted quiera inge: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Es un año bisiesto.")
else:
    print("No es un año bisiesto.")

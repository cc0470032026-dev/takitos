##Ejercicio 2:
# Solicita la edad de una persona y muestra si es menor de edad, mayor de edad o adulto mayor (60 o más).

edad = int(input("Ingresar su edad: "))

if edad >= 60:
    print("Eres adulto mayor.")
elif edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

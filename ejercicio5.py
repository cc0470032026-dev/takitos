##Ejercicio 5:
##Solicita dos números y una operación (+, -, *, /) y realiza el cálculo usando if, elif y else.

n1 = float(input("Primer número: "))
n2 = float(input("Segundo número: "))
op = input("Senior inge que quiere hacer (+, -, *, /): ")

if op == "+":
    print(f"Resultado: {n1 + n2}")
elif op == "-":
    print(f"Resultado: {n1 - n2}")
elif op == "*":
    print(f"Resultado: {n1 * n2}")
elif op == "/":
    if n2 != 0:
        print(f"Resultado: {n1 / n2}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida.")

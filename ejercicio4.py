## Elaborar un programa que llene un arreglo con 8 números ingresados por el usuario
# y mediante una función, determine cuál es el número mayor.


def encontrar_mayor(lista):
    mayor = lista[0]
    for num in lista:
        if num > mayor:
            mayor = num
    return mayor


datos = []
print("Ingrese 8 números:")
for i in range(8):
    n = int(input(f"Número {i+1}: "))
    datos.append(n)

print(f"El número más grande es {encontrar_mayor(datos)} increible")

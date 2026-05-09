##  Diseñar una función que reciba un arreglo de números
# y retorne un nuevo arreglo solo con los números positivos usando un bucle y condicionales.


def obtener_positivos(lista):
    positivos = []
    for num in lista:
        if num > 0:
            positivos.append(num)
    return positivos


entrada = input(
    "Ingrese números (positivos y negativos) pero estos separados algo asi -3 5: "
)
numeros = [int(n) for n in entrada.split()]
print(f"bit bot nueva lista solo con positivos: {obtener_positivos(numeros)}")

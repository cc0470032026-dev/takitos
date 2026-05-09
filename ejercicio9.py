##Elaborar una función que reciba un arreglo de números
# y devuelva la suma total, pero solo sumando los números pares.


def suma_pares(lista):
    suma = 0
    for n in lista:
        if n % 2 == 0:
            suma += n
    return suma


entrada = input(
    "Ingrese una lista de números para sumar solo los pares pero separados: "
)
numeros = [int(n) for n in entrada.split()]
print(f"La suma total de los pares es: {suma_pares(numeros)}")

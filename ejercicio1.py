##1. Crear una función que reciba una lista de números
# y retorne la cantidad de números pares e impares utilizando un bucle
# y estructuras condicionales.


def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"Resultados -> Pares: {pares}, Impares: {impares}")


entrada = input("Ponga numeros pero despues de cada uno separado: ")
numeros = [int(n) for n in entrada.split()]
contar_pares_impares(numeros)

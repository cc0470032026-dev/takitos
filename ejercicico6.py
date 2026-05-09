##Crear un programa que genere 10 números aleatorios,
# los guarde en un arreglo y mediante una función indique cuántos son mayores a 50.


import random


def contar_mayores_50(lista):
    contador = 0
    for n in lista:
        if n > 50:
            contador += 1
    return contador


aleatorios = [random.randint(1, 100) for _ in range(10)]
print(f"Números generados: {aleatorios}")
print(
    f"esta cantidad son mayores, no menores de 50 papu : {contar_mayores_50(aleatorios)}"
)

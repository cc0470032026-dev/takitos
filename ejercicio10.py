##Diseñar un programa que permita ingresar 6 números en un arreglo
# y mediante una función ordenarlos de menor a mayor usando ciclos e instrucciones condicionales.


def ordenar_lista(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


numeros_ordenar = []
print("Digame 6 números para ordenarlos:")
for i in range(6):
    num = int(input(f"Número {i+1}: "))
    numeros_ordenar.append(num)

print(f"Lista ordenada de menor a mayor: {ordenar_lista(numeros_ordenar)}")

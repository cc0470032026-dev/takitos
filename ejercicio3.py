##Crear una función que reciba un arreglo de notas y devuelva el promedio.
#  Además, usando if, indicar si el grupo aprueba o reprueba


def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    print(f"\nPromedio final: {promedio:.2f}")
    if promedio >= 6:
        print("EL GRUPO APRUEBA")
    else:
        print("EL GRUPO REPRUEBA")


entrada = input("ponga las notas del grupo pero separadas porfis: ")
notas = [float(n) for n in entrada.split()]
calcular_promedio(notas)

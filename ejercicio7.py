##Desarrollar una función que reciba un arreglo de edades
# y determine cuántas personas son mayores de edad utilizando if y un ciclo.


def contar_adultos(edades):
    adultos = 0
    for edad in edades:
        if edad >= 18:
            adultos += 1
    return adultos


entrada = input("Ingrese las edades pero siempre separadas inge: ")
edades_lista = [int(e) for e in entrada.split()]
print(f"Estas personas son mayores de edad: {contar_adultos(edades_lista)}")

## Desarrollar un programa que permita ingresar 10 nombres en un arreglo
#  y luego, mediante una función, muestre solo los nombres que tengan más de 5 caracteres


def filtrar_nombres(lista_nombres):
    print("\nNombres con más de 5 caracteres:")
    for nombre in lista_nombres:
        if len(nombre) > 5:
            print(f"- {nombre}")


nombres = []
for i in range(10):
    nom = input(
        f"Ingrese los nombres inge, cera tedioso pero vale la pena GG {i+1} de 10: "
    )
    nombres.append(nom)

filtrar_nombres(nombres)

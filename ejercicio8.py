##  Crear un programa que almacene 5 productos en un arreglo
#  y mediante una función busque un producto específico ingresado por el usuario.


def buscar_producto(lista, objetivo):
    encontrado = False
    for p in lista:
        if p.lower() == objetivo.lower():
            encontrado = True
            break
    if encontrado:
        print(f"¡El producto '{objetivo}' está disponible!")
    else:
        print("Que mal, el producto no fue encontrado.")


productos = []
print("Registre 5 productos en el sistema:")
for i in range(5):
    p = input(f"Producto {i+1}: ")
    productos.append(p)

busqueda = input("\n¿Qué producto quiere buscar?: ")
buscar_producto(productos, busqueda)

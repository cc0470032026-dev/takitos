##Ejercicio 7:
##Solicita el monto de una compra y aplica:
##Más de 100: 20% de descuento
##Entre 50 y 100: 10% de descuento
##Menos de 50: sin descuento

monto = float(input("Monto de la compra: "))

if monto > 100:
    final = monto * 0.80
    print(f"Descuento del 20%. Total: ${final}")
elif monto >= 50:
    final = monto * 0.90
    print(f"Descuento del 10%. Total: ${final}")
else:
    print(f"Sin descuento. Total: ${monto}")

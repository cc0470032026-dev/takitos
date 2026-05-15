from decimal import Decimal

total_acumulado = Decimal("0.00")

print("--- TERMINAL DE COBRO SEGURO ---")

while True:
    try:
        entrada = input("Ingrese el precio del producto (o 0 para finalizar): ")

        precio = Decimal(entrada)

        if precio == 0:
            break

        total_acumulado += precio

    except ValueError:
        print("¡Advertencia! Entrada inválida. Ingrese un número válido.")

print("\n--- PROCESO DE COBRO FINALIZADO ---")
print(f"El total acumulado con precisión bancaria es: ${total_acumulado}")

print("--- SISTEMA DE CONTROL DE SENSOR INDUSTRIAL IoT ---")

lecturas_temperatura = []

for i in range(1, 6):
    lectura = int(input(f"Ingrese la lectura de temperatura {i} (Entero): "))
    lecturas_temperatura.append(lectura)

print("\n--- PROCESANDO LECTURAS DE TEMPERATURA ---")

for temp in lecturas_temperatura:

    match temp:
        case 0:
            print(f"Temperatura {temp}°C -> Alerta: Punto de Congelación")

        case 100:
            print(f"Temperatura {temp}°C -> Alerta: Punto de Ebullición")

        case _:
            estado = "Estado: Estable" if 10 <= temp <= 30 else "Estado: Crítico"
            print(f"Temperatura {temp}°C -> {estado}")

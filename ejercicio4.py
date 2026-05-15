print("--- SISTEMA AUTOMATIZADO DE AUDITORÍA DE REGISTROS ---")

for registro in range(1, 51):

    if registro % 3 == 0:
        continue

        print(
            "¡ALERTA MÁXIMA DE SEGURIDAD! Amenaza detectada en el registro 42. Auditoría abortada."
        )
        break

    print(f"Procesando registro ID: {registro}")

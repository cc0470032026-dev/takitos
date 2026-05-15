print("--- SISTEMA DE CLASIFICACIÓN DE ENVÍOS ---")

etiqueta = input(
    "Ingrese el código de rastreo el formato debe de ser: AÑO-CATEGORÍA-PAÍS separados por un - : "
)

if etiqueta:
    primer_guion = etiqueta.find("-") + 1
    segundo_guion = etiqueta.rfind("-")
    categoria = etiqueta[primer_guion:segundo_guion]

    print(f"Categoría del paquete extraída: {categoria}")

    pais = etiqueta[-2:]

    ruta = "Ruta Local" if pais == "SV" else "Ruta Internacional"

    print(f"Destino asignado: {ruta}")

else:
    print("Error de seguridad: La entrada no puede estar vacía. Programa finalizado.")

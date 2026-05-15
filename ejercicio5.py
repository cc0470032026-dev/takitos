print("--- SISTEMA DE PRIVACIDAD Y OFUSCACIÓN DE DATOS ---")

nombre_completo = input("Ingrese su nombre completo (Nombre y Apellido): ")

palabras_originales = nombre_completo.split()

lista_invertida = palabras_originales[::-1]

print("\n--- Resultado de la Ofuscación por Privacidad ---")

for palabra in lista_invertida:

    letras_formateadas = []

    for letra in palabra:

        letras_formateadas.append(letra)

    palabra_ofuscada = ".".join(letras_formateadas)

    print(palabra_ofuscada, end=" ")

print()

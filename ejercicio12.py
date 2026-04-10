nombre_archivo = "ING. william.txt"

sin_extension = nombre_archivo.removesuffix(".txt")
limpio = sin_extension.removeprefix("ING. ")

resultado = limpio.lower()

print("Nombre de archivo:", resultado)

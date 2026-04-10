texto = "Python2026"

alfanumerico = texto.isalnum()

if alfanumerico:

    minusculas = texto.lower()

    resultado = minusculas.replace("2026", "")

    print("Resultado:", resultado)
else:
    print("El texto tiene simbolos o espacios.")

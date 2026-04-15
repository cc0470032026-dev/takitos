##Ejercicio 10:
##Pide usuario y contraseña. Si ambos coinciden con valores predefinidos, muestra "Acceso permitido", de lo contrario "Acceso denegado".

USUARIO_REGISTRADO = "william"
CONTRASENA_REGISTRADA = "1234"

usuario = input("Usuario: ")
contrasena = input("Contraseña: ")

if usuario == USUARIO_REGISTRADO and contrasena == CONTRASENA_REGISTRADA:
    print("Acceso permitido, vienvenido")
else:
    print("Acceso denegado")

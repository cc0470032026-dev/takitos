import random

dificultad = input("Elija la dificultad de esta salsa (1:Fácil, 2:Difícil): ")
match dificultad:
    case "1":
        limite = 10
    case _:
        limite = 100

numeros = [random.randint(1, limite) for i in range(3)]
print(f"Números generados: {numeros}")

intentos = 3
while intentos > 0:
    num = int(input("Adivina un número par de la lista: "))

    if num in numeros and num % 2 == 0:
        print("Estas en lo correcto papi es par.")
        break
    else:
        intentos -= 1
        print(f"noooo. ahora te quedan {intentos} intentos.")

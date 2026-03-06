Algoritmo CompararNumeros10
    Definir numx, numy Como Real
    Escribir "Ingrese un numero para comparar"
    Leer numx
    Escribir "Ingrese el segundo número:"
    Leer numy
    
    Si numx > numy Entonces
        Escribir "El mayor es: ", numx
        Escribir "El menor es: ", numy
    SiNo
        Si numx < numy Entonces
            Escribir "El mayor es: ", numy
            Escribir "El menor es: ", numx
        SiNo
            Escribir "Ambos números son iguales."
        FinSi
    FinSi
FinAlgoritmo
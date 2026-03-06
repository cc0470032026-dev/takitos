Algoritmo NumerosPares4
    Definir N, i, contador Como Entero
    
    Escribir "Saber cuántos números pares deseas ver:"
    Leer N
    
    Escribir "Los primeros ", N, " números pares son:"
    
    contador <- 1
    Para i <- 2 Hasta (N * 2) Con Paso 2 Hacer
        Escribir contador, ": ", i
        contador <- contador + 1
    FinPara
    
FinAlgoritmo
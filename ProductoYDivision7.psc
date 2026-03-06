Algoritmo ProductoYDivision7
	Definir numx, numy, producto, cociente Como Real
	
	Escribir "Ingresa el primer número:"
	Leer numx
	Escribir "Ingresa el segundo número:"
	Leer numy
	
	producto <- numx * numy
	Escribir "El producto (multiplicación) es: ", producto
	
	Si num2 <> 0 Entonces
		cociente <- numx / numy
		Escribir "El cociente (división) es: ", cociente
	Sino
		Escribir "Error: No se puede dividir entre cero."
	FinSi
FinAlgoritmo

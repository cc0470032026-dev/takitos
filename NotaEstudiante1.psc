Algoritmo NotaEstudiante1
	Definir nota Como Real
	
	Repetir
		Escribir "Ingrese la nota del estudiante (0 a 10):"
		Leer nota
		Si nota < 0 O nota > 10 Entonces
			Escribir "disculpe profe, la nota debe estar en el rango de 0 a 10."
		FinSi
	Hasta Que nota >= 0 Y nota <= 10
	
	Si nota >= 6 Entonces
		Escribir "Resultado: APROBADO"
	Sino
		Si nota >= 5 Entonces
			Escribir "Resultado: RECUPERACIÓN"
		Sino
			Escribir "Resultado: REPROBADO"
		FinSi
	FinSi
	
FinAlgoritmo
